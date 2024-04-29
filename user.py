from bank_name import bank
from datetime import datetime
from Bank import Bank
from create_account import Account

class User(Account):
    def __init__(self, name, email, address, account_type, password):
        super().__init__(name, email, address, account_type, password)
        self.transection_history = []
        self.loans = 0
        self.loans_count = 0
        self.account_id = self.generate_account_number(name, email)
        Bank.users.append(self)

    def deposit(self, bank, amount, account_id):
        account = bank.find_account(account_id)
        if account:
            if amount > 0:
                account.balance += amount
                bank.balance += amount
                print(f'You successfully deposited {amount}.')
                self.transection_history.append(f"{datetime.now()} Deposit: {amount}")
            else:
                print('Invalid deposit amount.')
        else:
            print("Account not found.")

    def withdraw(self, bank, amount, account_id):
        account = bank.find_account(account_id)
        if account:
            if account.balance >= amount and amount > 0:
                if bank.bank_status == True:
                    print("Bank is bankrupt")
                    return
                account.balance -= amount
                bank.balance -= amount
                print(f"Withdrew {amount}.")
                self.transection_history.append(f"{datetime.now()} withdraw {amount}")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Account not found.")

    def show_available_balance(self, bank, account_id):
        account = bank.find_account(account_id)
        if account:
            print(f"{self.name} your account Balance is {account.balance}")
        else:
            print("Account not found.")

    def check_history(self, account_id):
        account = bank.find_account(account_id)
        if account:
            print("***** Transaction History *****")
            print(f"*** Date ***\t\t\t*** Amount ***")
            for history in self.transection_history:
                print(history)
        else:
            print("Account not found.")

    def transfer_money(self, bank, amount, sender_account, recipient_account):
        sender = bank.find_account(sender_account)
        recipient = bank.find_account(recipient_account)
        if sender and recipient:
            if sender.balance >= amount:
                sender.balance -= amount
                recipient.balance += amount
                print(f"{amount} tk successfully transfer to {recipient_account}")
                self.transection_history.append(f"From {sender_account} transfer {amount} to {recipient_account}")
            else:
                print("Invaild amount!")
        else:
            print("Account does not exist!")

    def take_loan(self, bank, amount, account_id):
        account = bank.find_account(account_id)
        if account:
            if self.loans_count < 2 and bank.balance >= amount and bank.bank_status==False and amount>0 and bank.loan_status==True:
                self.loans_count += 1
                account.balance += amount
                bank.balance -= amount
                self.loans += amount
                print(f"Loan {amount} taken successfully!")
            else:
                print("Sorry, your loan request rejected!")
        else:
            print("Account not found.")
