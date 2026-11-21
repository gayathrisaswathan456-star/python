class Bankaccount:
    def __init__(self, acc_no, name, acc_type,balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited:",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("amount withdraw:",amount)
        else:
            print("insufficient balance")

    def display(self):
        print("\nAccount details")
        print("account number:",self.acc_no)
        print("name:",self.name)
        print("Account type:",self.acc_type)
        print("balance:",self.balance)

acc = Bankaccount(101, "anu" , "savings",5000)
acc.display()
acc.deposit(2000)
acc.withdraw(1500)
acc.display()
