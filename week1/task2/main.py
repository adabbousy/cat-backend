def main():
    print_choices()
    balance = 1000

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            balance = deposit(balance)
            check_balance(balance)

        elif choice == 3:
            balance = withdraw(balance)
            check_balance(balance)

        elif choice == 4:
            print("Thank you for using Simple Bank System!")
            break

def print_choices():
    print("""Welcome to Simple Bank System!
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
""")


def check_balance(balance):
    print(f"Your balance is: {balance:.2f}\n")


def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Deposit amount must be a positive number.")
            return balance
        print("Deposit successful!")
        return balance + amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance



def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal amount must be a positive number.")
            return balance
        if amount > balance:
            print("Insufficient balance!")
            return balance
        print("Withdrawal successful!")
        return balance - amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance


if __name__ == "__main__":
    main()