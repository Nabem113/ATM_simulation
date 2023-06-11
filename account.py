class Account:

    def __init__(self):
        self.accountBalance = 1000000

    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount

    def withdraw(self, amount):
        self.accountBalance = self.accountBalance - amount
