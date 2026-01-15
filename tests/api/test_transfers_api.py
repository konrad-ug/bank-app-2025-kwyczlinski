import pytest
import requests

class TestAPI:
    url = "http://localhost:5000/api"
    
    @pytest.fixture(autouse=True)
    def set_up(self):
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "John",
            "last_name": "Doe", 
            "pesel": "81010200131"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"

        url = f"{self.url}/accounts/81010200131/transfer"
        payload = {
            "amount": 100.0,
            "type": "incoming"
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert response.json()["message"] == "Zlecenie przyjęto do realizacji"

        yield
        all_accounts = requests.get(f"{self.url}/accounts").json()
        for account in all_accounts:
            requests.delete(f'{self.url}/accounts/{account["pesel"]}')

    @pytest.mark.parametrize("payload, pesel, expected_code, expected_balance", [
        ({"amount":100.0, "type":"incoming"}, "81010200131", 200, 200.0),
        ({"amount":50.0,  "type":"outgoing"}, "81010200131", 200, 50.0),
        ({"amount":50.0,  "type":"express" }, "81010200131", 200, 49.0),
        ({"amount":100.0, "type":"express" }, "81010200131", 200, -1.0),
        ({"amount":500.0, "type":"outgoing"}, "81010200131", 422, 100.0),
        ({"amount":20.0,  "type":"incoming"}, "12345678910", 404, 100.0),
        ({"amount":-20.0, "type":"outgoing"}, "81010200131", 422, 100.0),
        ({"amount":-20.0, "type":"incoming"}, "81010200131", 422, 100.0),
        ({"amount":20.0,  "type":"robbery!"}, "81010200131", 400, 100.0),
        ({"amount":None,  "type":"incoming"}, "81010200131", 400, 100.0),
        ({"type":"incoming"}, "81010200131", 400, 100.0),
        ({"amount":20.0}, "81010200131", 400, 100.0),
        ({"amount":20.0,  "type":"incoming", "pesel":"81010200131"}, "81010200131", 200, 120.0),
        ({}, "81010200131", 400, 100.0),
    ], ids=[
        "incoming transfer",
        "outgoing transfer",
        "express transfer",
        "express gets negative",
        "outgoing too much",
        "account doesnt exist",
        "negative amount outgoing",
        "negative amount incoming",
        "non-recognizable type",
        "bad amount type",
        "payload missing amount",
        "payload missing type",
        "payload contains garbage",
        "empty payload",
    ])
    def test_transfers(self, payload, pesel, expected_code, expected_balance):
        url = f"{self.url}/accounts/{pesel}/transfer"
        response = requests.post(url, json=payload)

        assert response.status_code == expected_code
        
        if (expected_code == 200):
            url = f"{self.url}/accounts/{pesel}"
            response = requests.get(url)
            account = response.json()
            assert account["balance"] == expected_balance
