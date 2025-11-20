from src.personal_account import PersonalAccount
import pytest

class TestPersonalLoan:
    @pytest.fixture()
    def account(self):
        account = PersonalAccount("John", "Doe", "81010200131")
        return account

    @pytest.mark.parametrize("history, amount, expected_result, expected_balance", [
        ([40.0, 40.0, 40.0], 500.0, True, 500.0),
        ([200.0, 200.0, -10.0, -10.0, -10.0], 230.0, True, 230.0),
        ([200.0, 200.0, -40.0, -40.0, -40.0], 500.0, False, 0.0),
        ([200.0], 20.0, False, 0.0),
        ([200.0, 200.0, 200.0, -100.0], 20.0, False, 0.0),
        ([200.0, -150.0, 100.0, -10.0, -10.0, -10.0, 50.0], 100.0, True, 100.0),
        ([10.0, 10.0, -10.0, 10.0, 10.0], 40.0, False, 0.0),
        ([10.0, 10.0, 10.0], -10.0, False, 0.0),
        ([[10.0, 10.0, 10.0, 10.0]], True, False, 0.0)
    ],
    ids=[
        "three positive",
        "last five greater than loan",
        "too big loan",
        "less than three entries",
        "less than five entries",
        "last five entries",
        "exact amount",
        "negative amount",
        "amount type bool"
    ])
    def test_personal_loan(self, account, history: list[float], amount: float, expected_result: bool, expected_balance: float):
        account.history = history
        assert account.submit_for_loan(amount) == expected_result
        assert account.balance == expected_balance