class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.attempts = 0

    def withdraw(self, amount):

        self.balance = self.balance - amount

        if self.balance <= 0:
            self.balance = self.balance + amount
            print(">> Low Balance:", self.balance, ". Can not Withdraw")
            self.attempts += 1

        else:
            print(">> Withdraw Success. New Balance:", self.balance)

        if self.attempts == 3:
             iRef = IndexError("Illegal Attempts")
             raise iRef

print(">> Welcome")
print(">> Banking Started")

bRef = BankAccount()

for _ in range(1000):
    bRef.withdraw(3000)

print(">> Banking Finished")