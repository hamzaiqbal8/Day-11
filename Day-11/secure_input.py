""" Ask for user age and handle invalid inputs using try/except"""

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Invalid input! Please enter a number.")
