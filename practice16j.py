# BankingException is a class which we created and is he child of Exception
class BankingError(Exception):
    pass


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
            bRef = BankingError("Illegal Attempts")
            raise bRef


print(">> Welcome")
print(">> Banking Started")

bRef = BankAccount()
try:
    for _ in range(1000):
        bRef.withdraw(3000)

except BankingError as ref:
    print("Some Error occured")

print(">> Banking Finished")

# Crash will not occur here