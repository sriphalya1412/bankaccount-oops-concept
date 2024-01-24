# bankaccount-oops-concept
#with methods of withdrawl,deposit,displaying the balance
class BankAccount:
    def _init_(self, accountholdername, accountnumber, balance=500):
        self.accountholdername = accountholdername
        self.accountnumber = accountnumber
        self.balance = balance

    def deposit_money(self, money):
        self.balance += money
        return self.balance

    def current_balance(self):
        return self.balance

    def withdraw_money(self, money):
        if money > self.balance:
            return "Insufficient balance"
        self.balance -= money
        return money
