from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

class TestAccountRegistry:
    @pytest.fixture()
    def registry(self):
        registry = AccountRegistry()
        return registry

    @pytest.mark.parametrize("accounts, searched_pesel, expected_search_result", [
        ([PersonalAccount("John", "Doe", "12345678910")], "12345678910", PersonalAccount("John", "Doe", "12345678910")),
        ([PersonalAccount("Jenna", "Doe", "10987654321"), PersonalAccount("John", "Doe", "12345678910")], "12345678910", PersonalAccount("John", "Doe", "12345678910")),
        ([PersonalAccount("John", "Doe", "12345678910")], "10987654321", None),
        ([], "12345678910", None)
    ], ids=[
        "one account and found",
        "multiple accouts and found",
        "account not found",
        "empty"
    ])
    def test_account_registry(self, registry: AccountRegistry, accounts: list[PersonalAccount], searched_pesel: str, expected_search_result: bool):
        for account in accounts:
            registry.add_account(account)
        
        assert registry.all_accounts() == accounts
        assert registry.count() == len(accounts)
        assert registry.accounts == accounts
        if expected_search_result is None:
            assert registry.find(searched_pesel) is None
        else:
            assert registry.find(searched_pesel).__dict__ == expected_search_result.__dict__


    @pytest.mark.parametrize("accounts, to_remove, expected_registry", [
        ([PersonalAccount("John", "Doe", "12345678910")], ["12345678910"], [PersonalAccount("John", "Doe", "12345678910")]),
        ([PersonalAccount("Jenna", "Doe", "10987654321"), PersonalAccount("John", "Doe", "12345678910")], ["12345678910"], [PersonalAccount("Jenna", "Doe", "10987654321")]),
        ([PersonalAccount("Jenna", "Doe", "10987654321"), PersonalAccount("John", "Doe", "12345678910")], ["10987654321","12345678910"], []),
        ([PersonalAccount("John", "Doe", "12345678910")], ["12345678910"], []),
        ([], "12345678910", [])
    ], ids=[
        "no one account deleted",
        "multiple accouts and one deleted",
        "multiple accouts deleted",
        "deleted only account",
        "no account to delete"
    ])
    def test_account_registy_delete(self, registry: AccountRegistry, accounts: list[PersonalAccount], to_remove: list[str], expected_registry: list[PersonalAccount]):
        for account in accounts:
            registry.add_account(account)

        end_registry = AccountRegistry()
        for acc in expected_registry:
            end_registry.add_account(acc)
    
        assert registry.all_accounts() == accounts
        assert end_registry.all_accounts() == expected_registry

        for pesel in to_remove:
            registry.delete(pesel)
        
        for acc in registry.all_accounts():
            assert registry.find(acc.pesel).__dict__ == registry.find(acc.pesel).__dict__
