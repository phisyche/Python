class BankAccount(object):

  def __init__(self, balance=3000):
    self.balance = balance

  def deposit(self, cash_dep_amount):
    self.balance = cash_dep_amount + self.balance

  def withdraw(self, cash_wit_amount):
    self.balance = self.balance - cash_wit_amount
    if(cash_wit_amount > self.balance):
      return "invalid transaction"

class MinimumBalanceAccount(BankAccount):
  def __init__(self):
    print "Min bal"
