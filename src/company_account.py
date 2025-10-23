from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name : str, nip : str):
        super().__init__()
        self.company_name = company_name
        self.nip = nip if (self.is_nip_valid(nip)) else "Invalid"

    def is_nip_valid(self, nip : str) -> bool:
        return True if (isinstance(nip, str) and len(nip) == 10) else False