from bank import Bank
from account import Account


    
def user_menu(bank):
    while True:
        account_number = int(input("Enter your account number: "))
        if account_number in bank.accounts:
            customer = bank.accounts[account_number]
            break
        else:
            print("Invalid account number. Please try again.")

    while True:
        print(f"\nWelcome {customer.name}!!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == 3:
            customer.check_balance()
        elif choice == 4:
            customer.view_transaction_history()
        elif choice == 5:
            amount = float(input("Enter loan amount: "))
            customer.take_loan(amount, bank)
        elif choice == 6:
            target_account_number = int(input("Enter target account number: "))
            amount = float(input("Enter amount to transfer: "))
            customer.transfer(amount, target_account_number, bank)
        elif choice == 7:
            break
        else:
            print("Invalid Input")

def admin_menu(bank):
    while True:
        print(f"\nWelcome Admin!!")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Show Users")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Turn Off Loan Feature")
        print("7. Turn On Loan Feature")
        print("8. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == 3:
            bank.show_users()
        elif choice == 4:
            bank.total_bank_balance()
        elif choice == 5:
            bank.total_bank_loan()
        elif choice == 6:
            bank.off_loan()
        elif choice == 7:
            bank.on_loan()
        elif choice == 8:
            break
        else:
            print("Invalid Input")

def main_menu():
    bank = Bank()
    while True:
        print("\nWelcome!!")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_menu(bank)
        elif choice == 2:
            admin_menu(bank)
        elif choice == 3:
            break
        else:
            print("Invalid Input")
bank = Bank()
while True:
        print("\nWelcome!!")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_menu(bank)
        elif choice == 2:
            admin_menu(bank)
        elif choice == 3:
            break
        else:
            print("Invalid Input")