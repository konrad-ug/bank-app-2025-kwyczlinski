class Account:
    def __init__(self):
        self.balance : float = 0.0
        self.history : list[float] = []

    def incomming_transfer(self, amount : float) -> None:
        if (isinstance(amount, float) and amount >= 0):
            self.balance += amount
            self.history.append(amount)

    def outgoing_transfer(self, amount : float) -> None:
        if (isinstance(amount, float) and amount >= 0 and self.balance >= amount):
            self.balance -= amount
            self.history.append(-amount)


    def express_outgoing_transfer(self, amount : float, fee : float) -> None:
        if (isinstance(amount, float) and amount >= 0 and self.balance >= amount):
            self.balance -= amount + fee
            self.history.append(-amount)
            self.history.append(-fee)

    def test_coverage(self):
        pass
