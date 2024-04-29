from bank_name import bank
from Admin import Admin
def admin_id():
    
    
    while True:      
        print("1. Show all user account")
        print("2. Delete bank account")
        print("3. Total balance of bank")
        print("4. Total amount of loan")
        print("5. Loan feature")
        print("6. Sign in")
        print("7. Sign out")
        choice=int(input("Choice the option: "))
                
        if choice==1:
            owner.see_all_user_account_list(bank)
        elif choice==2:
            id=input("Enter the user id: ")
            owner.delete_user(bank,id)
        elif choice==3:
            owner.show_bank_balance(bank)
        elif choice==4:
            owner.show_total_loans_amount(bank)
        elif choice==5:
            op=bool(input("Enter True or False so that on or off loan feature: "))
            owner.loan_feature(bank,op)
        elif choice==6:       
          name=input("Enter your name: ")
          email=input("Enter your email: ")
          address=input("Enter your address: ")
          account_type=input("Enter the type of account: ")
          password=input("Enter your password: ")
          owner=Admin(name=name,email=email,address=address,account_type=account_type,password=password)
          print(f"Account created successfully! ")
        elif choice==7:
            break
        else:
            print("Invaild choice !!!")
      
   
          