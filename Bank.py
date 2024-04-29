class Bank:
    users=[]
    admin=[]
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.bank_status=False
        self.loan_feature = True

    @classmethod
    def find_account(cls,id):
        for account in cls.users:
            if account.account_id==id:
                return account
        return None
    
    def show_all_users(self):
        print("Name:\tBalance\tAccount_id")
        for user in self.users:
            print(f"{user.name}\t{user.balance}\t{user.account_id}")
    
    def delete_user(self,id):
        user=self.find_account(id)
        if user:
            self.users.remove(user)
            print("Account deleted successfully.")
        else:
            print("Bank account not found.")
    def show_balance(self):
        print(f"The bank have {self.balance} tk ")
    
    def total_loans(self):
        total=0
        for user in self.users:
            total+=user.loans
        return total
    
    def loan_status(self, status):
        self.loan_feature = status


        



