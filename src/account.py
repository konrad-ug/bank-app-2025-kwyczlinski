from src.smtp.smtp import SMTPClient
import datetime

class Account:
    express_outgoing_transfer_fee : float = 0.0
    history_email_prefix: str = ""

    def __init__(self):
        self.balance : float = 0.0
        self.history : list[float] = []

    def incomming_transfer(self, amount : float) -> bool:
        if not (isinstance(amount, float) and amount >= 0):
            return False
            
        self.balance += amount
        self.history.append(amount)
        return True

    def outgoing_transfer(self, amount : float) -> bool:
        if not (isinstance(amount, float) and amount >= 0 and self.balance >= amount):
            return False

        self.balance -= amount
        self.history.append(-amount)
        return True

    def express_outgoing_transfer(self, amount : float) -> bool:
        if not (isinstance(amount, float) and amount >= 0 and self.balance >= amount):
            return False
        
        self.balance -= amount + self.express_outgoing_transfer_fee
        self.history.append(-amount)
        self.history.append(-self.express_outgoing_transfer_fee)
        return True

    def send_history_via_email(self, email_address: str) -> bool:
        smtp = SMTPClient()

        subject = f'Account Transfer History {datetime.date.today().strftime("%Y-%m-%d")}'
        text = f"{self.history_email_prefix} {self.history}"
        
        return smtp.send(subject, text, email_address)