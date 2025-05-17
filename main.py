from services import BankServices
from Exception import *
import getpass

def main():
    bank = BankServices()  # <-- FIXED here

    while True:
        print("----------------------Welcome to ICDC Unsecure Bank----------------")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Logout")
        print("6. Check balance")
        print("7. Exit")

        choice = input("Enter your Choice: ")
        try:
            if choice == "1":
                acc_number = input("Enter Account Number: ")
                name = input("Enter Your Name: ")
                pin = input("Set 4-digit Password: ")
                print(bank.create_account(acc_number, name, pin))

            elif choice == "2":
                acc_number = input("Enter Account Number: ")
                pin = input("Enter 4-digit Password: ")
                print(bank.login(acc_number, pin))

            elif choice == "3":
                amount = float(input("Enter The Amount: "))
                print(bank.deposit(amount))  # corrected typo "deposite" → "deposit"

            elif choice == "4":
                amount = float(input("Enter The Amount: "))
                print(bank.withdraw(amount))  # corrected typo "withdrow" → "withdraw"

            elif choice == "5":
                print(bank.logout())

            elif choice == "6":
                print(bank.check_balance())

            elif choice == "7":
                print("Thank you for using our services")
                break

            else:
                print("Invalid choice, please try")

        except Exception as e:
            print(f"Something Goes Wrong {e}")

main()
