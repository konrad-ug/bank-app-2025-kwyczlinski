from src.personal_account import PersonalAccount

class TestTransfers:
    def test_incomming_transfer(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.incomming_transfer(20.0)
        assert account.balance == 20.0

    def test_incomming_negative(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.incomming_transfer(-20.0)
        assert account.balance == 0.0

    def test_incomming_wrong_type_str(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.incomming_transfer("money")
        assert account.balance == 0.0

    def test_incomming_wrong_type_bool(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.incomming_transfer(True)
        assert account.balance == 0.0

    def test_incomming_wrong_type_none(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.incomming_transfer(None)
        assert account.balance == 0.0

    def test_outgoing_transfer(self):
        account = PersonalAccount("John", "Doe", "81010200131") #1. set up
        account.balance = 100.0 #1. set up

        account.outgoing_transfer(20.0) #2. action

        assert account.balance == 80.0 #3. assertion

    def test_outgoing_exceeding_balance(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.balance = 50.0
        account.outgoing_transfer(100.0)
        assert account.balance == 50.0

    def test_outgoing_negative(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.outgoing_transfer(-50.0)
        assert account.balance == 0.0

    def test_outgoing_wrong_type_str(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.balance = 100.0
        account.outgoing_transfer("money")
        assert account.balance == 100.0

    def test_outgoing_wrong_type_bool(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.balance = 100.0
        account.outgoing_transfer(True)
        assert account.balance == 100.0

    def test_outgoing_wrong_type_none(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        account.balance = 100.0
        account.outgoing_transfer(None)
        assert account.balance == 100.0