from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest

class TestTransfers:
    @pytest.fixture()
    def account(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        return account

    @pytest.mark.parametrize("amount, expected_balance, expected_history", [
        (20.0, 20.0, [20.0]),
        (-20.0, 0.0, []),
        ("money", 0.0, []),
        (True, 0.0, []),
        (None, 0.0, [])
    ],
    ids=[
        "correct incoming transfer",
        "incoming negative",
        "incoming amount wrong type str",
        "incoming amount wrong type bool",
        "incoming amount wrong type None"
    ])
    def test_transfers_incoming(self, account, amount: float, expected_balance: float, expected_history: list[float]):
        account.incomming_transfer(amount)
        assert account.balance == expected_balance
        assert account.history == expected_history

    @pytest.mark.parametrize("balance, amount, expected_balance, expected_history", [
        (100.0, 20.0, 80.0, [-20.0]),
        (50.0, 100.0, 50.0, []),
        (0.0, -50.0, 0.0, []),
        (100.0, "money", 100.0, []),
        (100.0, True, 100.0, []),
        (100.0, None, 100.0, [])
    ],
    ids=[
        "correct outgoing transfer",
        "outgoing exceeding balance",
        "outgoing negative",
        "outgoing amount wrong type str",
        "outgoing amount wrong type bool",
        "outgoing amount wrong type None"
    ]
    )
    def test_transfers_outgoing(self, account, balance: float, amount: float, expected_balance: float, expected_history: list[float]):
        account.balance = balance
        account.outgoing_transfer(amount)
        assert account.balance == expected_balance
        assert account.history == expected_history

class TestExpressTransfers:
    @pytest.fixture()
    def personal_account(self):
        personal_account = PersonalAccount("John", "Doe", "81010200131")
        return personal_account
    
    @pytest.fixture()
    def company_account(self, mocker):
        mock_verify_nip_api = mocker.Mock()
        mock_verify_nip_api.verify_nip_api.return_value = True
        mocker.patch.object(CompanyAccount, "verify_nip_api", new_callable=mock_verify_nip_api)

        company_account = CompanyAccount("Deere & Company", "0123456789")
        return company_account

    @pytest.mark.parametrize("balance, amount, expected_balance, expected_history", [
        (50.0, 40.0, 9.0, [-40.0, -1.0]),
        (50.0, 50.0, -1.0, [-50.0, -1.0])
    ],
    ids=[
        "correct personal express",
        "personal express dept"
    ])
    def test_personal_express(self, personal_account, balance: float, amount: float, expected_balance: float, expected_history: list[float]):
        personal_account.balance = balance
        personal_account.express_outgoing_transfer(amount)
        assert personal_account.balance == expected_balance
        assert personal_account.history == expected_history

    @pytest.mark.parametrize("balance, amount, expected_balance, expected_history", [
        (50.0, 40.0, 5.0, [-40.0, -5.0]),
        (50.0, 50.0, -5.0, [-50.0, -5.0]),
        (100.0, True, 100.0, [])
    ],
    ids=[
        "correct company express",
        "company express dept",
        "express amount wrong type bool"
    ])
    def test_company_express(self, company_account, balance: float, amount: float, expected_balance: float, expected_history: list[float]):
        company_account.balance = balance
        company_account.express_outgoing_transfer(amount)
        assert company_account.balance == expected_balance
        assert company_account.history == expected_history
