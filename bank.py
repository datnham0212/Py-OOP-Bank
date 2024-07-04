class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        if (amount > self.balance):
            print('Insufficient funds')
        else:
            self.balance -= amount

    def info(self):
        print(f"Name: {self.name}\nBalance: ${self.balance}")


