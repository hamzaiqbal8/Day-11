"""cli_assistant_v2.py"""

import datetime


responses = {
    "help": """
Available commands:
- time       → Show current time
- date       → Show today's date
- joke       → Tell a joke
- convert    → Convert cm/inches
- help       → Show this help message
- exit       → Exit the assistant
""",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
}


print("Welcome to CLI Assistant v2!")
print("Type 'help' to see the list of commands.\n")

while True:
    command = input(">> Enter command: ").strip().lower()

    try:
        if command == "time":
            now = datetime.datetime.now().strftime("%I:%M %p")
            print("Current time:", now)

        elif command == "date":
            today = datetime.date.today().strftime("%B %d, %Y")
            print("Today's date:", today)

        elif command == "convert":
            unit = input("Type 'cm' to convert to inches or 'inches' to convert to cm: ").strip().lower()

            if unit == "cm":
                cm = float(input("Enter length in cm: "))
                inches = cm / 2.54
                print(f"{cm} cm = {round(inches, 2)} inches")

            elif unit == "inches":
                inches = float(input("Enter length in inches: "))
                cm = inches * 2.54
                print(f"{inches} inches = {round(cm, 2)} cm")

            else:
                print("Invalid conversion type! Use 'cm' or 'inches'.")

        elif command in responses:
            print(responses[command])

        elif command == "exit":
            print("Exiting CLI Assistant. Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' to see available commands.")

    except Exception as e:
        print("Error:", str(e))
