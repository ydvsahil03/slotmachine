import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 30

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],  end="|")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much you want to deposit :")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("enter a number")

    return amount


def get_lines():
    while True:
        lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines ")
        else:
            print("enter a number")

    return lines


def get_bet():
    while True:
        bet = input("How much you want to bet :")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"BET must be between {MIN_BET} and {MAX_BET} ")
        else:
            print("enter a number")

    return bet


def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"Your balance is ${bet}on {lines} lines . total bet is equal to: {total_bet} ")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
