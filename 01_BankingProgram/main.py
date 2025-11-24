def show_balance(balance):
    text_decoration()
    print(f"Your balance is ${balance:.2f}")
    text_decoration()
    text_decoration()

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Thats not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:"))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater or equal to 0.")
        return 0
    else:
        return amount

def text_decoration():
    print("-"*25)


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Bank Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            text_decoration()
            print("That is not a valid choice")
            text_decoration()

    text_decoration()
    print("Thank you! Have a nice day!")
    text_decoration()


if __name__ == "__main__":
    main()