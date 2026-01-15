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
    def test_company_account_creation(self, mocker, company_name: str, nip: str, expected_nip: str, expected_balance: float):
        mock_verify_nip_api = mocker.Mock()
        mock_verify_nip_api.verify_nip_api.return_value = True
        mocker.patch.object(CompanyAccount, "verify_nip_api", new_callable=mock_verify_nip_api)
        
        account = CompanyAccount(company_name, nip)
        
        assert account.nip == expected_nip
        assert account.balance == expected_balance

    def test_company_account_creation_error(self, mocker):
        mocker.patch.object(
            CompanyAccount,
            "is_nip_valid",
            return_value=True,
        )

        mocker.patch.object(
            CompanyAccount,
            "verify_nip_api",
            return_value=False,
        )

        with pytest.raises(ValueError, match="Company not registered!!"):
            CompanyAccount("Deere & Company", "012345678910")

