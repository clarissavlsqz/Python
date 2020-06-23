class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdrawl(self, amount):
        if amount > self.balance:
            print("The amount to withdrawl is bigger than the actual balance, try with a smaller amount")
        else:
            self.balance -= amount
            print("Withdrawl accepted")

    def __str__(self):
        return ("Account owner: {}\n".format(self.owner) + "Account balance: {}".format(self.balance))

acct1 = BankAccount('Clari', 100)
print(acct1)
acct1.deposit(50)
print(acct1)
acct1.withdrawl(75)
print(acct1)
acct1.withdrawl(500)
print(acct1)
