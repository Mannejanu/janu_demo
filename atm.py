"""Create a class BankAccount with:
account holder name
balance

Add methods:

deposit
withdraw
display balance"""
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        print("account holder is",self.account_holder)
        print("balance initially",self.balance)
    def deposit(self,deposit_amount):
        self.balance=self.balance+deposit_amount
        print("balance after deposit",self.balance)
    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-withdraw_amount
            print("balance after withdraw",self.balance)
        
        
    def display_balance(self):
        print("balance after transactions",self.balance)
obj1=BankAccount("janu",75000) 
obj1.deposit(10000)
obj1.withdraw(5000)
obj1.display_balance()     
        