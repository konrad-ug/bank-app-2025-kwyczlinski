class Account:
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        self.pesel = pesel if (self.is_pesel_valid(pesel)) else "Invalid"

    def is_pesel_valid(self, pesel):
        return True if(isinstance(pesel, str) and len(pesel) == 11) else False
