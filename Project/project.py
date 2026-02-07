# file handling -> 
import os 
from abc import ABC,abstractmethod

# Abstract class (Abstraction)
class Account(ABC):
    # constructor
    def __init__(self,account_number , owner, balance =0):
        self.account_number = account_number
        self.owner = owner
        # private variable -> 
        self.__balance = balance
    
    # Abstract Method
    @abstractmethod
    def withdraw(self,amount):
        pass

    def deposit(self,amount):
        # money provide bank
        if(amount > 0):
            self.__balance += amount  
            print(f"Deposited {amount}. New Balance is {self.__balance}")

        else:
            print(f"Invalid Deposit amount")

    def getBalance(self):
        return self.__balance
    

    def set_balance(self,newBalance):
        self.__balance = newBalance


    # str -> dunder __function__ -> str -> display collectively in the format of string
    def __str__(self):
        return f"Account [{self.account_number}] - Owner : {self.owner.name} , Balance : {self.__balance}"
    
# Polymorphism + Inheritance
class SavingAccount(Account):
    # saving account ki implementation apke abstract method de rhe ho 
    def withdraw(self, amount):
       if(amount <= self.getBalance()):
           self.set_balance(self.getBalance()- amount)
           print(f"Withdraw {amount}. New Balance is {self.getBalance()}")
       else:
           print("Insufficient Funds in your Account")

class CurrentAccount(Account):


    def __init__(self, account_number, owner, balance=0,od_limit = 50000):
        # parent ki implementation -> constructor se hai
        super().__init__(account_number, owner, balance)
        # child ne ek argument khud intialize krliya 
        self.od_limit = od_limit
        

    def withdraw(self, amount):
       if amount <= self.getBalance() + self.od_limit:
            self.set_balance(self.getBalance() - amount) 
            print(f"Withdraw {amount}. New Balance is {self.getBalance()}")
       else:
           print("Insufficient Funds in your Account and Overdraft limit exceeded")

class Customer:
    def __init__(self,name,cID):
        self.name = name
        self.customerID = cID

    def __str__(self):
            return f" ( Customer name :  {self.name}) ,(Id : {self.customerID})"


# Bank Class with file handling

class Bank:
    def __init__(self, filename = "Project/account.txt"):
        # collection
        self.accounts = {}
        self.filename = filename
        self.load_account()



    def create_Account(self,account_type , account_number , owner):
        if account_type == "savings":
            account = SavingAccount(account_number,owner)
        elif account_type == 'current':
             account = CurrentAccount(account_number,owner)
        else:
            print("invalid Account type")
            return
        
        self.accounts[account_number] = account
        # data ko file m save
        self.save_accounts() 
        print(f"{account_type.capitalize()} account created for {owner.name} ")


    def get_account(self,account_number):
        return self.accounts.get(account_number, None)
    
    # accounts se file 
    def save_accounts(self):
        with open(self.filename, "w") as f:
            for acc in self.accounts.values():
                acc_type = acc.__class__.__name__
                f.write(f"{acc_type},{acc.account_number},{acc.owner.name},{acc.owner.customerID},{acc.getBalance()}\n")


    # user se accounts 
    def load_account(self):
        if not os.path.exists(self.filename):
            return 
        with open(self.filename , "r") as f:
            for l in f:
                acc_type , acc_no, name , customerID , balance = l.strip().split(",")
                owner = Customer(name , int(customerID))

                if acc_type == "SavingAccount":
                    acc = SavingAccount(int(acc_no) , owner , float(balance))
                else:
                    acc = CurrentAccount(int(acc_no) , owner , float(balance))

                # collections ke andr store ho rkha hai
                self.accounts[(int(acc_no))] = acc


# starter

if __name__ == "__main__":
    bank = Bank()



    while(True):
        print("\n ---- Bank Menu ---- ")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money in Account")
        print("4. Withdraw Money from Account")
        print("5. Check Balance from Account")
        print("6. Exit")



        choice = (input("Enter your Choice : \n"))

        if(choice == "1"):
            name = input("Enter Customer Name : ")
            cID = int(input("Enter Customer Id : "))
            acc_no = int(input("Enter Account number : "))
            bank.create_Account("savings",acc_no,Customer(name,cID))

        elif choice == "2":
            name = input("Enter Customer Name : ")
            cID = int(input("Enter Customer Id : "))
            acc_no = int(input("Enter Account number : "))
            bank.create_Account("current",acc_no,Customer(name,cID))
            
        elif choice == "3":
            acc_no = int(input("Enter Account number : "))
            amount = int(input("Enter amount : "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.deposit(amount)
                bank.save_accounts()
            else:
                print("Account not found")
                
        elif choice == "4":
            acc_no = int(input("Enter Account number : "))
            amount = int(input("Enter amount : "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.withdraw(amount)
                bank.save_accounts()
            else:
                print("Account not found")

        elif choice == "5":
            acc_no = int(input("Enter Account number : "))
            acc = bank.get_account(acc_no)
            if acc:
                print(f'Balance for Account -: ({acc_no}) = {acc.getBalance()}')
            else:
                print("Account not found")


        elif choice == "6":
           print("Exit.... Thank you for Banking wit us!!!!")
           break

        else:
            print("Invalid Choice--- Please try again")
            
            