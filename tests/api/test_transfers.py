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

    @pytest.mark.parametrize("amount, type, pesel, expected_code, expected_balance", [
        (100.0, "incoming", "81010200131", 200, 200.0),
        (50.0, "outgoing", "81010200131", 200, 50.0),
        (50.0, "express", "81010200131", 200, 49.0),
        (100.0, "express", "81010200131", 200, -1.0),
        (500.0, "outgoing", "81010200131", 422, 100.0),
        (20.0, "incoming", "12345678910", 404, 100.0),
        (-20.0, "outgoing", "81010200131", 422, 100.0),
        (-20.0, "incoming", "81010200131", 422, 100.0),
        (20.0, "robbery!", "81010200131", 400, 100.0),
    ], ids=[
        "incoming transfer",
        "outgoing transfer",
        "express transfer",
        "express gets negative",
        "outgoing too much",
        "account doesnt exist",
        "negative amount outgoing",
        "negative amount incoming",
        "non recognizable type",
    ])
    def test_transfers(self, amount, type, pesel, expected_code, expected_balance):
        url = f"{self.url}/accounts/{pesel}/transfer"
        payload = {
            "amount": amount,
            "type": type
        }
        response = requests.post(url, json=payload)

        assert response.status_code == expected_code
        
        if (expected_code == 200):
            url = f"{self.url}/accounts/{pesel}"
            response = requests.get(url)
            account = response.json()
            assert account["balance"] == expected_balance