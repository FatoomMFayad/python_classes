class BankAccount:
    accountNumber = 0
    name = ""
    balance = 0

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def bankFees(self):
        bank_fees = self.balance * 0.05
        return bank_fees

    def display(self):
        print(f"Account Number: {self.accountNumber}, Name: {self.name}, Balance: {self.balance}, bank fees: {self.bankFees()}")

bank_account = BankAccount(1234, "Fatoom", 100)
bank_account.display()
bank_account.deposit(100)
bank_account.display()
bank_account.withdraw(10)
bank_account.display()