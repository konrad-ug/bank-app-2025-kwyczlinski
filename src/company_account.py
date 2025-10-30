from src.account import Account

class CompanyAccount(Account):
    express_outgoing_transfer_fee : float = 5.0 

    def __init__(self, company_name : str, nip : str):
        super().__init__()
        self.company_name : str = company_name
        self.nip : str = nip if (self.is_nip_valid(nip)) else "Invalid"
        self.fee_amount : float = 5.0

    def is_nip_valid(self, nip : str) -> bool:
        return True if (isinstance(nip, str) and len(nip) == 10) else False
