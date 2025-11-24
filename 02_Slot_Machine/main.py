import random

def spin_row():
    symbols = ['🍇', '🍉', '🥝']
    result = [random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("*"*10)
    print(" | ".join(row))
    print("*"*10)

def get_payout(row, bet):
    if row[0]==row[1] and row[1]==row[2]:
        if row[0]=='🍇':
            return bet * 3
        if row[0]=='🍉':
            return bet * 4
        if row[0] == '🥝':
            return bet * 5
    return 0

def main():
    balance = 100
    print("-"*25)
    print("Welcome to Slot Machine")
    print("Symbols: 🍇 🍉 🥝")
    print("-"*25)
    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place your bet amount")
        print(bet)
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry You lost this round")
        balance += payout
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print("*"*30)
    print(f"Game Over! Your final balance is ${balance}")
    print("*"*30)

if __name__ == "__main__":
    main()