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
        yield
        all_accounts = requests.get(f"{self.url}/accounts").json()
        for account in all_accounts:
            requests.delete(f'{self.url}/accounts/{account["pesel"]}')

    def test_get_account_count(self):
        url = f"{self.url}/accounts/count"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["count"] == 1

    @pytest.mark.parametrize("pesel, expected_code", [
        ("81010200131", 200),
        ("12345678910", 404),
    ], ids=[
        "Account exists",
        "Account does not exist"
    ])
    def test_get_account_by_pesel(self, pesel, expected_code):
        url = f"{self.url}/accounts/{pesel}"
        response = requests.get(url)
        assert response.status_code == expected_code

    @pytest.mark.parametrize("pesel, first_name, last_name, expected_code", [
        ("81010200131", "Johannes", "Douglas", 200),
        ("81010200131", "Johannes", None, 200),
        ("81010200131", None, "Douglas", 200),
        ("81010200131", None, None, 200),
        ("12345678910", "Johannes", "Douglas", 404),

    ], ids=[
        "Update first and second name",
        "Update only first name",
        "Update only second name",
        "Update none but account exists",
        "Account does not exist"
    ])
    def test_update_account(self, pesel, first_name, last_name, expected_code):
        url = f"{self.url}/accounts/{pesel}"
        payload = {
            "first_name": first_name,
            "last_name": last_name, 
        }
        response = requests.patch(url, json=payload)

        assert response.status_code == expected_code

        if (expected_code == 200):
            response = requests.get(url)
            assert response.status_code == 200
            if (first_name):
                assert response.json()["first_name"] == first_name
            if (last_name):
                assert response.json()["last_name"] == last_name

    @pytest.mark.parametrize("pesel, expected_code", [
        ("12345678910", 404),
        ("81010200131", 200),
    ], ids=[
        "Account does not exist",
        "Account deleted successfully",

    ])
    def test_delete_account(self, pesel, expected_code):
        url = f"{self.url}/accounts/{pesel}"
        response = requests.delete(url)
        assert response.status_code == expected_code

    def test_succesfull_delete_account(self):
        url = f"{self.url}/accounts/{81010200131}"
        response = requests.delete(url)
        assert response.status_code == 200

        response = requests.delete(url)
        assert response.status_code == 404

    def test_account_already_exists(self):
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "pesel": "81010200131"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Account with this pesel already exists"
