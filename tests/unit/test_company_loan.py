# from src.company_account import CompanyAccount
# import pytest

# class TestCompanyLoan:
#     @pytest.fixture()
#     def account(self, mocker):
#         mocker.patch.object(CompanyAccount, "verify_nip_api", new_callable=mocker.PropertyMock, return_value=True)
#         account = CompanyAccount("Deere & Company", "0123456789")
#         return account
    

#     @pytest.mark.parametrize("amount, history, balance, expected_result, expected_balance", [
#         (1000.0, [2000.0, -1775.0], 2000.0, True, 3000.0),
#         (100.0, [400.0], 400.0, False, 400.0),
#         (2000.0, [-1775], 1000.0, False, 1000.0),
#         (0.0, [], 0.0, False, 0.0),
#         (1000.0, [-5, -1775, -1775, -5, -5], 4000.0, True, 5000.0),
#         ("1000.0", [6000, -1775, -20, -5, -200], 4000.0, False, 4000.0),
#         (None, [6000, -1775, -20, -5, -200], 4000.0, False, 4000.0),
#         (True, [6000, -1775, -20, -5, -200], 4000.0, False, 4000.0),
#         (-2000.0, [6000, -1775, -20, -5, -200], 4000.0, False, 4000.0)
#     ], ids=[
#         "minimal balance",
#         "insurance not payed",
#         "balance too small",
#         "empty account",
#         "many insurance payments",
#         "amount wrong type str",
#         "amount wrong type None",
#         "amount wrong type bool",
#         "negative amount"
#     ])
#     def test_company_loan(self, account, amount: float, history: list[float], balance: float, expected_result: bool, expected_balance: float):
#         account.history = history
#         account.balance = balance
#         assert account.take_loan(amount) == expected_result
#         assert account.balance == expected_balance