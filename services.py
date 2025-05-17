from model import Account
from database import BankDatabase
from Exception import *

class BankServices:
    def __init__(self):
        self.db = BankDatabase()
        self.logged_in_account = None

    def create_account(self, acc_number, name, pin):
        if self.db.get_account(acc_number):
            raise AccountAlreadyExisted("Account Already Exists")
        acc = Account(acc_number, name, pin)
        self.db.add_account(acc)
        return "Account created successfully."

    def login(self, acc_num, pin):
        account = self.db.get_account(acc_num)
        if account:
            if account.pin == pin:
                self.logged_in_account = account
                return f"Welcome {account.name}"
            else:
                raise PasswordIncorrectException("Incorrect Password")
        else:
            raise AccountNotFound("Account not found")

    def deposit(self, amount):
        if self.logged_in_account:
            self.logged_in_account.balance += amount
            return f"Deposited {amount}"
        else:
            raise NotLoggedIn("Please log in first")

    def withdraw(self, amount):
        if self.logged_in_account:
            if self.logged_in_account.balance >= amount:
                self.logged_in_account.balance -= amount
                return f"Withdrew {amount}"
            else:
                raise InsufficientBalanceException("Insufficient balance")
        else:
            raise NotLoggedIn("Please log in first")

    def check_balance(self):
        if self.logged_in_account:
            return f"Current balance: {self.logged_in_account.balance}"
        else:
            raise NotLoggedIn("Please log in first")

    def logout(self):
        self.logged_in_account = None
        return "Logged out successfully."
