from src.company_account import CompanyAccount
import pytest

class TestCompanyAccount:
    @pytest.mark.parametrize("company_name, nip, expected_nip, expected_balance", [
        ("Deere & Company", "0123456789", "0123456789", 0.0),
        ("Deere & Company", "012456789", "Invalid", 0.0),
        ("Deere & Company", "012345670089", "Invalid", 0.0),
        ("Deere & Company", "None", "Invalid", 0.0),
    ],
    ids=[
        "correct data",
        "nip too short",
        "nip too long",
        "nip is none"
    ])
    def test_company_account_creation(self, company_name: str, nip: str, expected_nip: str, expected_balance: float):
        account = CompanyAccount(company_name, nip)
        assert account.nip == expected_nip
        assert account.balance == expected_balance