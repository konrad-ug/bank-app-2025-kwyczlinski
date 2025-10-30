from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name : str, nip : str):
        super().__init__()
        self.company_name : str = company_name
        self.nip : str = nip if (self.is_nip_valid(nip)) else "Invalid"
        self.fee_amount : float = 5.0

    def is_nip_valid(self, nip : str) -> bool:
        return True if (isinstance(nip, str) and len(nip) == 10) else False
    
    def express_outgoing_transfer(self, amount : float) -> None:
        return super().express_outgoing_transfer(amount, self.fee_amount)
    