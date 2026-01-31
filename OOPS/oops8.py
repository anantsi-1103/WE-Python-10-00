from abc import ABC, abstractmethod


class BankAccount(ABC):

    # function  ko bus create krthe ho
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass
    
    @abstractmethod
    def checkBalance(self):
        pass


class Account(BankAccount):
# balanace -> bal
    # constructor -> special method jo auto execute jesi ap us class ka object create krthe ho
    def __init__(self , bal):
       self.balance = bal

# implementation yaha pr hoti hai -> 
    def deposit(self, amount):
      self.balance += amount
      print(f"Deposited Amount {amount} and your balance is {self.balance}")

    def withdraw(self, amount):
      if amount <= self.balance:
         self.balance -= amount
         print(f"Withdraw Amount {amount} and your balance is {self.balance}")
      else:
         print("Insufficient Balance")

    def checkBalance(self):
       print(f"Current Balance is {self.balance}")



acc = Account(10000)

# user ne kaam kra 
acc.deposit(3000)
acc.withdraw(2000)
acc.withdraw(4000)
acc.deposit(8000)
acc.withdraw(1000)

acc.checkBalance()