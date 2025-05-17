from model import Account
class BankDatabase:

    def __init__(self):
        self.accounts={}

    def add_account(self,ac):
        self.accounts[ac.acc_number]=ac
        print("Account added successfully")

    def get_account(self,acc_num):
        return self.accounts.get(acc_num)

    def authenticate(self,acc_num,pin):
        acc=self.get_account(acc_num)
        if acc and acc.pin==pin:
            return acc
        else:
            return None