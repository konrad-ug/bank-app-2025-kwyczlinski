from src.company_account import CompanyAccount

class TestAccount:
    def test_account_creation(self):
        account = CompanyAccount("Deere & Company", "0123456789")
        assert account.balance == 0
        assert account.nip == "0123456789"

    def test_nip_too_short(self):
        account = CompanyAccount("Deere & Company", "012456789")
        assert account.nip == "Invalid"

    def test_nip_too_long(self):
        account = CompanyAccount("Deere & Company", "012345670089")
        assert account.nip == "Invalid"

    def test_nip_is_none(self):
        account = CompanyAccount("Deere & Company", None)
        assert account.nip == "Invalid"
        assert account.balance == 0
