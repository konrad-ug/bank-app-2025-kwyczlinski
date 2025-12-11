from src.personal_account import PersonalAccount

class AccountRegistry:
    def __init__(self) -> None:
        self.accounts = []

    def add_account(self, account: PersonalAccount) -> None:
        self.accounts.append(account)

    def find(self, pesel: str) -> PersonalAccount | None:
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
    
    def all_accounts(self) -> list[PersonalAccount]:
        return self.accounts
    
    def count(self) -> int:
        num = len(self.accounts)
        return num
    
    def delete(self, pesel) -> None:
        if (self.find(pesel)):
            self.accounts.remove(self.find(pesel))
        return None

    
