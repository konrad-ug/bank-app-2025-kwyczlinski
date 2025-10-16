from src.account import Account

class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "81010200131")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "81010200131"

    def test_pesel_too_short(self):
        account = Account("John", "Doe", "810131")
        assert account.pesel == "Invalid"

    def test_pesel_too_long(self):
        account = Account("John", "Doe", "8101010102000131")
        assert account.pesel == "Invalid"

    def test_pesel_is_none(self):
        account = Account("John", "Doe", None)
        assert account.pesel == "Invalid"

    def test_pesel_is_none(self):
        account = Account("John", "Doe", True)
        assert account.pesel == "Invalid"

    def test_promo_code_is(self):
        account = Account("John", "Doe", "81010200131", promo_code="PROM_M#1")
        assert account.balance == 50
    
    def test_promo_code_invalid(self):
        account = Account("John", "Doe", "81010200131", promo_code="Prom_122")
        assert account.balance == 0