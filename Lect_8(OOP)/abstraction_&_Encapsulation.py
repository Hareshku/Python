class Account:
    def __init__(self, account=234567, balance =0):
        self.account= account
        self.balance = balance
        print(account, balance)

    def Debit(self, amount):
        self.balance-=amount
        print("Rs: ", amount, "debited \n remaining balance is", self.getBalance)

    def Credit(self, amount):
        self.balance+=amount
        print("Rs: ", amount, "is credited into your account. \n Now new balance is Rs: ", self.getBalance())

    def getBalance(self):
        return self.balance


acout1 = Account(224232323, 10000)
print(acout1.getBalance())

