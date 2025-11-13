from src.personal_account import PersonalAccount
class TestPersonalLoan:
    def test_three_incoming(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [400.0, 400.0, 400.0]
        assert account.submit_for_loan(500.0) == True
        assert account.balance == 500.0

    def test_last_five_greater_than_loan(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [200.0, 200.0, -10.0, -10.0, -10.0]
        assert account.submit_for_loan(230.0) == True
        assert account.balance == 230.0

    def test_too_big_loan(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [200.0, 200.0, -40.0, -40.0, -40.0]
        assert account.submit_for_loan(500.0) == False
        assert account.balance == 0.0

    def test_not_enought_three_incoming(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [200.0]
        assert account.submit_for_loan(20.0) == False
        assert account.balance == 0.0
    
    def test_not_enought_transactions_last_five(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [200.0, 200.0, 200.0, -100.0]
        assert account.submit_for_loan(20.0) == False
        assert account.balance == 0.0

    def test_checks_last_five(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [200.0, -150.0, 100.0, -10.0, -10.0, -10.0, 50.0]
        assert account.submit_for_loan(100.0) == True
        assert account.balance == 100.0

    def test_exact_amount(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [10.0, 10.0, -10.0, 10.0, 10.0]
        assert account.submit_for_loan(40.0) == False
        assert account.balance == 0.0

    def test_negative_amount(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [10.0, 10.0, 10.0]
        assert account.submit_for_loan(-10.0) == False
        assert account.balance == 0.0

    def test_bad_type(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.history = [10.0, 10.0, 10.0, 10.0]
        assert account.submit_for_loan(True) == False
        assert account.balance == 0.0