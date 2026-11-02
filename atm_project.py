import json
import os


FILE_NAME = "atm_data.json"


# --------------------------------------------
# 1. Create default account / Load account
# --------------------------------------------

print ("=================================")
print("Welcome to Python  Bank ATM" )
print("==================================")

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    data = {
        "customer_name": "Akshaya",
        "pin": "2006" ,
        "balance": 50000,
        "history": []
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    return data


# --------------------------------------------
# 2. Save data
# --------------------------------------------

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# --------------------------------------------
# 3. PIN Verification
# --------------------------------------------

def verify_pin(data):
    attempts = 3

    while attempts > 0:
        pin = input("Enter your PIN: ")

        if pin == data["pin"]:
            print("\nLogin successful!")
            print(f"Welcome, {data['customer_name']}!")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
        else:
            print("\nCard blocked!")
            return False

    return False


# --------------------------------------------
# 4. Check Balance
# --------------------------------------------

def check_balance(data):
    print(f"\nCurrent Balance: Rs. {data['balance']}")


# --------------------------------------------
# 5. Deposit Money
# --------------------------------------------

def deposit_money(data):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        data["balance"] += amount

        data["history"].append(
            f"Deposited Rs. {amount:g}"
        )

        save_data(data)

        print(f"Rs. {amount:g} deposited successfully.")
        print(f"Updated Balance: Rs. {data['balance']:g}")

    except ValueError:
        print("Invalid amount. Please enter a number.")


# --------------------------------------------
# 6. Withdraw Money
# --------------------------------------------

def withdraw_money(data):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > data["balance"]:
            print("Insufficient balance.")
            return

        data["balance"] -= amount

        data["history"].append(
            f"Withdrew Rs. {amount:g}"
        )

        save_data(data)

        print(f"Rs. {amount:g} withdrawn successfully.")
        print(f"Updated Balance: Rs. {data['balance']:g}")

    except ValueError:
        print("Invalid amount. Please enter a number.")


# --------------------------------------------
# 7. Transaction History
# --------------------------------------------

def transaction_history(data):
    print("\n---------- Transaction History ----------")

    if len(data["history"]) == 0:
        print("No transactions yet.")
        return

    for i, transaction in enumerate(data["history"], start=1):
        print(f"{i}. {transaction}")


# --------------------------------------------
# 8. Main Menu
# --------------------------------------------

def main_menu(data):
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            check_balance(data)

        elif choice == "2":
            deposit_money(data)

        elif choice == "3":
            withdraw_money(data)

        elif choice == "4":
            transaction_history(data)

        elif choice == "5":
            print("\nThank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# --------------------------------------------
# 9. Main Program
# --------------------------------------------

def main():
    data = load_data()

    if verify_pin(data):
        main_menu(data)


# Start the program
main()