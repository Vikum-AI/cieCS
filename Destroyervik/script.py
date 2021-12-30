# Withdraw money, deposit money, transfer
balanceGlobal = 30000


class bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("You successfull withdrawn $", amount, "from your account")
        print("Remaining balance is $", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("You successfull deposited $", amount, "from your account")
        print("Remaining balance is $", self.balance)

    def transfer(self, amount, name):
        self.balance = self.balance - amount
        print("You successfull transferred $", amount, "to", name)
        print("Remaining balance is $", self.balance)


d = bank(30000)
print("")
d.withdraw(5000)
print("")
d.deposit(2000)
print("")
d.transfer(1000, 'Elon')
print("")
