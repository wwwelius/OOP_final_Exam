class Bank:
    total_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            Bank.total_balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance. Bank is bankrupt.")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received: {amount} from {self.name}")
        else:
            print("Insufficient balance. Bank is bankrupt.")

    def take_loan(self):
        if Bank.loan_feature_enabled:
            loan_amount = 2 * self.balance
            self.balance += loan_amount
            Bank.total_balance += loan_amount
            Bank.total_loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        else:
            print("Loan feature is currently disabled.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history


class Admin:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, balance):
        account = Bank(name, balance)
        self.accounts.append(account)
        return account

    def check_total_balance(self):
        return Bank.total_balance

    def check_total_loan_amount(self):
        return Bank.total_loan_amount

    def enable_loan_feature(self):
        Bank.loan_feature_enabled = True

    def disable_loan_feature(self):
        Bank.loan_feature_enabled = False


def main():
    admin = Admin()

    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Take Loan")
        print("8. Check Total Bank Balance")
        print("9. Check Total Loan Amount")
        print("10. Enable Loan Feature")
        print("11. Disable Loan Feature")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter account holder's name: ")
            balance = float(input("Enter initial balance: "))
            account = admin.create_account(name, balance)
            print(f"Account created successfully. Account Number: {account.name}")

        elif choice == 2:
            account_name = input("Enter account holder's name: ")
            amount = float(input("Enter amount to deposit: "))
            account = next((acc for acc in admin.accounts if acc.name == account_name), None)
            if account:
                account.deposit(amount)
                print("Amount deposited successfully.")
            else:
                print("Account not found.")

        elif choice == 3:
            account_name = input("Enter account holder's name: ")
            amount = float(input("Enter amount to withdraw: "))
            account = next((acc for acc in admin.accounts if acc.name == account_name), None)
            if account:
                account.withdraw(amount)
                print("Amount withdrawn successfully.")
            else:
                print("Account not found.")

        elif choice == 4:
            sender_name = input("Enter sender's account holder's name: ")
            recipient_name = input("Enter recipient's account holder's name: ")
            amount = float(input("Enter amount to transfer: "))
            sender = next((acc for acc in admin.accounts if acc.name == sender_name), None)
            recipient = next((acc for acc in admin.accounts if acc.name == recipient_name), None)
            if sender and recipient:
                sender.transfer(recipient, amount)
                print("Amount transferred successfully.")
            else:
                print("Account not found.")

        elif choice == 5:
            account_name = input("Enter account holder's name: ")
            account = next((acc for acc in admin.accounts if acc.name == account_name), None)
            if account:
                print("Account Balance:", account.check_balance())
            else:
                print("Account not found.")

        elif choice == 6:
            account_name = input("Enter account holder's name: ")
            account = next((acc for acc in admin.accounts if acc.name == account_name), None)
            if account:
                print("Transaction History:", account.check_transaction_history())
            else:
                print("Account not found.")

        elif choice == 7:
            account_name = input("Enter account holder's name: ")
            account = next((acc for acc in admin.accounts if acc.name == account_name), None)
            if account:
                account.take_loan()
                print("Loan taken successfully.")
            else:
                print("Account not found.")

        elif choice == 8:
            print("Total Bank Balance:", admin.check_total_balance())

        elif choice == 9:
            print("Total Loan Amount:", admin.check_total_loan_amount())

        elif choice == 10:
            admin.enable_loan_feature()
            print("Loan feature enabled.")

        elif choice == 11:
            admin.disable_loan_feature()
            print("Loan feature disabled.")

        elif choice == 12:
            break

        print() 


if __name__ == "__main__":
    main()
