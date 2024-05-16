from account import Account

class Bank:
    next_account_number = 10000000  
    def __init__(self):
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True
        self.accounts = {}
    
    def create_account(self, name, email, address, account_type):
        account_number = Bank.next_account_number
        Bank.next_account_number += 1
        account = Account(name, email, address, account_type, account_number)
        self.accounts[account_number] = account
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number
    
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully!")
        else:
            print("Account not found.")
    
    def show_users(self):
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts in the bank.")
    
    def total_bank_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts.values())
        print(f"Total available balance in the bank: ${self.total_balance}")
    
    def total_bank_loan(self):
        print(f"Total loan amount given by the bank: ${self.total_loan}")
    
    def off_loan(self):
        self.loan_feature = False
        print("Loan feature is now off.")
    
    def on_loan(self):
        self.loan_feature = True
        print("Loan feature is now on.")
