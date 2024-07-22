import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    print(logo)

def get_bid():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    return name, price

def find_winner(bids):
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}")

def main():
    display_logo()
    bids = {}
    while True:
        name, price = get_bid()
        bids[name] = price
        if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == 'no':
            break
        clear_console()
    find_winner(bids)

if __name__ == "__main__":
    main()
