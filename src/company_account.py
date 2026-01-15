from src.account import Account
from datetime import datetime
import requests

BANK_APP_MF_URL = "https://wl-test.mf.gov.pl"


class CompanyAccount(Account):
    express_outgoing_transfer_fee : float = 5.0 

    def __init__(self, company_name : str, nip : str):
        super().__init__()
        self.company_name : str = company_name
        self.fee_amount : float = 5.0
        self.nip : str = nip 
        if (not self.is_nip_valid(nip)):
            self.nip: str = "Invalid"
        elif not self.verify_nip_api(nip):
            raise ValueError("Company not registered!!")

    def is_nip_valid(self, nip : str) -> bool:
        return True if (isinstance(nip, str) and len(nip) == 10 ) else False

    def take_loan(self, amount: float) -> bool:
        if (isinstance(amount, float) and amount > 0 and self.balance >= 2*amount and self.history.__contains__(-1775)):
            self.balance += amount
            return True
        return False

    def verify_nip_api(self, nip) -> bool:
        url = f"{BANK_APP_MF_URL}/api/search/nip/{nip}?date={datetime.now().date()}"
        response = requests.get(url)

        return False if (not response.json() or not response.json()["result"] or not response.json()["result"]["subject"] or response.json()["result"]["subject"]["statusVat"] != "Czynny") else True