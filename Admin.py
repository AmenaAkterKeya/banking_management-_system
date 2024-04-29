from create_account import Account
from Bank import Bank
class Admin(Account):
    def __init__(self, name, email, address, account_type,password):
        super().__init__(name, email, address, account_type,password)
        Bank.admin.append(self)
    
    def see_all_user_account_list(self,bank):
        bank.show_all_users()
    def delete_user(self,bank,account_id):
        bank.delete_user(account_id)
    def show_bank_balance(self,bank):
       bank.show_balance()
    def show_total_loans_amount(self,bank):
        t=bank.total_loans()
        print(f"The bank have {t} tk ")
    def loan_feature(self,bank,status):
        bank.loan_status(status)
    