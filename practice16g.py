class BankAccount:

    def __init__(self):
        self.balance = 10000

    def withdraw(self, amount):

        self.balance = self.balance - amount

        if self.balance <= 0:
            self.balance = self.balance + amount
            print(">> Low Balance:", self.balance, ". Can not Withdraw")

        else:
            print(">> Withdraw Success. New Balance:", self.balance)


bRef = BankAccount()

for _ in range(1000):
    bRef.withdraw(3000)