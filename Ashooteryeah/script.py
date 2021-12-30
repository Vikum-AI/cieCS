

class bank:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,withdra):
        self.balance = self.balance - withdra
        print("You've successfully withdrawn",withdra,"from your account")
        print("Remaining balance is ",self.balance)

    def deposit(self,dep):
        self.balance = self.balance + dep
        print("You've successfully deposited ",dep,"to your account")
        print("Remaining balance is ",self.balance)

    def transferr(self,transf,name):
        self.balance = self.balance - transf
        print("You succcessfully transferred ",transf," to ",name)
        print("Remainin balance is ",self.balance)

b = bank(30000)
print("")

b.withdraw(5000)
print("")

b.deposit(2000)
print("")
b.transferr(1000, 'Elon')
print("")






