"""Convert inches to cm or Fahrenheit to Celsius with option selector"""

print("Choose conversion type:")
print("1. Inches to Centimeters")
print("2. Fahrenheit to Celsius")


choice = input("Enter 1 or 2: ")


if choice == "1":
    inches = float(input("Enter value in inches: "))
    cm = inches * 2.54
    print(f"{inches} inches = {cm} centimeters")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Invalid choice. Please enter 1 or 2.")
