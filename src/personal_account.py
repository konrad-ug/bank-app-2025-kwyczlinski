from src.account import Account

class PersonalAccount(Account):
    express_outgoing_transfer_fee : float = 1.0

    def __init__(self, first_name : str, last_name : str, pesel : str, promo_code : str | None = None):
        super().__init__()
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.pesel : str = pesel if (self.is_pesel_valid(pesel)) else "Invalid"
        self.balance : float = 50.0 if (self.is_pesel_valid(pesel)) and (self.is_promo_code_valid(promo_code) and self.is_not_too_old(pesel)) else 0.0
        self.fee_amount : float = 1.0

    def is_pesel_valid(self, pesel : str) -> bool:
        return True if (isinstance(pesel, str) and len(pesel) == 11) else False

    def is_promo_code_valid(self, promo_code : str) -> bool:
        return True if (isinstance(promo_code,str) and len(promo_code) == 8 and promo_code.startswith("PROM_")) else False

    def is_not_too_old(self, pesel : str) -> bool:
        if (self.is_pesel_valid(pesel)):
            if (int(pesel[2]) >= 2):
                yob = 2000 + int(pesel[0:2])
            else:
                yob = 1900 + int(pesel[0:2])
        
        return True if (yob > 1960) else False
