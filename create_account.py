import random
class Account:
    def __init__(self,name,email,address,account_type,password):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.password=password
        self.balance=0
        self.account_id=self.generate_account_number(name,email)
        
    def generate_account_number(self, name,email):
        random_number = str(random.randint(1, 100000))
        account_info = name[:4] + random_number[:4] + email[:3] 
        return account_info
    