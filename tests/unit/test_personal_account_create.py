from src.personal_account import PersonalAccount
import pytest

class TestPersonalAccount:

    # @pytest.fixture(autouse=True, scope="function")
    # def account(self):
    #     self.account = PersonalAccount("John", "Doe", "81010200131")
    #     # yield
    #     # del self.account

    # def test_account_creation(self):
    #     assert self.account.first_name == "John"
    #     assert self.account.last_name == "Doe"
    #     assert self.account.balance == 0
    #     assert self.account.pesel == "81010200131"

    # different way of use

    @pytest.mark.parametrize("first_name, last_name, pesel, promo_code, expected_pesel, expected_balance", [
        ("John", "Doe", "81010200131", None, "81010200131", 0.0),
        ("John", "Doe", "810131", None, "Invalid", 0.0),
        ("John", "Doe", "8101010102000131", None, "Invalid", 0.0),
        ("John", "Doe", None, "PROM_M#1", "Invalid", 0.0),
        ("John", "Doe", True, None, "Invalid", 0.0),
        ("John", "Doe", "81010200131", "PROM_M#1", "81010200131", 50.0),
        ("John", "Doe", "81010200131", "Prom_122", "81010200131", 0.0),
        ("John", "Doe", "44010200131", "PROM_M#1", "44010200131", 0.0),
        ("John", "Doe", "01201010101", "PROM_M#1", "01201010101", 50.0)
    ],
    ids=[
        "correct data",
        "pesel too short",
        "pesel too long",
        "pesel wrong type None",
        "pesel wrong type bool",
        "promo code correct",
        "promo code invalid",
        "too old for promo code",
        "young client new pesel promo code",
    ])
    def test_personal_account_creation(self, first_name: str, last_name: str, pesel: str, promo_code: str, expected_pesel: str, expected_balance: float):
        account = PersonalAccount(first_name, last_name, pesel, promo_code)
        assert account.first_name == first_name
        assert account.last_name == last_name
        assert account.pesel == expected_pesel
        assert account.balance == expected_balance
