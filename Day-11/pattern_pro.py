"""3. Challenge: Pattern Design Generator Pro"""

def colored(text, color_code):
    """3. Challenge: Pattern Design Generator Pro"""
    return f"\033[{color_code}m{text}\033[0m"

def print_square(rows, symbol, color):
    """3. Challenge: Pattern Design Generator Pro"""
    for _ in range(rows):
        print(colored(symbol * rows, color))

def print_pyramid(rows, symbol, color):
    """3. Challenge: Pattern Design Generator Pro"""
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = symbol * (2 * i - 1)
        print(colored(spaces + stars, color))

def print_diamond(rows, symbol, color):
    """3. Challenge: Pattern Design Generator Pro"""
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = symbol * (2 * i - 1)
        print(colored(spaces + stars, color))
    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (rows - i)
        stars = symbol * (2 * i - 1)
        print(colored(spaces + stars, color))

def print_hollow_rectangle(rows, symbol, color):
    """3. Challenge: Pattern Design Generator Pro"""
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(colored(symbol * rows, color))
        else:
            print(colored(symbol + ' ' * (rows - 2) + symbol, color))

def show_menu():
    """3. Challenge: Pattern Design Generator Pro"""
    print("""
Pattern Design Generator Pro
Choose a pattern:
1. Square
2. Pyramid
3. Diamond
4. Hollow Rectangle
5. Exit
""")

def choose_color():
    colors = {
        "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36"
    }
    print("Available colors:", ', '.join(colors.keys()))
    selected = input("Enter a color: ").strip().lower()
    return colors.get(selected, "37")  # Default to white if color not found

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "5":
        print("👋 Goodbye! Thanks for using Pattern Pro.")
        break

    rows = int(input("Enter number of rows: "))
    symbol = input("Enter symbol to use: ")
    color = choose_color()

    print("\nGenerated Pattern:\n")
    if choice == "1":
        print_square(rows, symbol, color)
    elif choice == "2":
        print_pyramid(rows, symbol, color)
    elif choice == "3":
        print_diamond(rows, symbol, color)
    elif choice == "4":
        print_hollow_rectangle(rows, symbol, color)
    else:
        print("❌ Invalid choice. Please try again.")
