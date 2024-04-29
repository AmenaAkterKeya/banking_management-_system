from user import User
from bank_name import bank
def User_id():
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Transfer money")
        print("6. Apply Loan")
        print("7. Sign in")
        print("8. Sign out")
        choice=int(input("Enter the option: "))
        
        if choice==1:
            account_id = input("Enter account number: ")
            customer.show_available_balance(bank,account_id)
        elif choice==2:
            account_id = input("Enter account number: ")
            money=int(input("Enter the deposit amount: "))
            customer.deposit(bank,money,account_id)
        elif choice==3:
            account_id = input("Enter account number: ")
            amount=int(input("Enter the amount for Withdraw: "))
            customer.withdraw(bank,amount,account_id)
            
        elif choice==4:
            account_id = input("Enter account number: ")
            customer.check_history(account_id)
        elif choice==5:
            sender_account = input("Enter your account number: ")
            recipient = input("Enter recipient's account number: ")
            amount = int(input("Enter amount to transfer: "))
            customer.transfer_money(bank,amount,sender_account,recipient)
        elif choice==6:
            account_id = input("Enter account number: ")
            amount = int(input("Enter amount to take as loan: "))
            customer.take_loan(bank,amount,account_id)
        elif choice==7:
            name=input("Enter your name: ")
            email=input("Enter your email: ")
            address=input("Enter your address: ")
            account_type=input("Enter your account type: ")
            password=input("Enter your password : ")
            customer=User(name=name,email=email,address=address,account_type=account_type,password=password)
            acc_id = customer.account_id
            print(f"Account created successfully! Your Acoount Id - {acc_id}")
        elif choice==8:
            break
        else:
            print("Invaild choice !!!")
    
    



