import datetime

class Account:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.loans_taken = 0
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append((datetime.datetime.now(), 'Deposit', amount))
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append((datetime.datetime.now(), 'Withdraw', amount))
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Available balance: ${self.balance}")
    
    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)
    
    def take_loan(self, amount, bank):
        if self.loans_taken >= 2:
            print("Loan limit reached")
        elif not bank.loan_feature:
            print("Loan feature is currently off")
        else:
            self.balance += amount
            bank.total_loan += amount
            self.loans_taken += 1
            self.transaction_history.append((datetime.datetime.now(), 'Loan', amount))
            print(f"Loan of ${amount} granted. New balance: ${self.balance}")
    
    def transfer(self, amount, target_account_number, bank):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        elif target_account_number not in bank.accounts:
            print("Account does not exist")
        else:
            self.balance -= amount
            bank.accounts[target_account_number].balance += amount
            self.transaction_history.append((datetime.datetime.now(), 'Transfer', amount))
            bank.accounts[target_account_number].transaction_history.append((datetime.datetime.now(), 'Received Transfer', amount))
            print(f"Transferred ${amount} to account {target_account_number}. New balance: ${self.balance}")
    
    def __str__(self):
        return f"Account({self.account_number}): {self.name}, {self.account_type}, Balance: ${self.balance}"
