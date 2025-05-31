"""Check if a given string is a palindrome (ignoring spaces/case)"""

text = input("Enter a string: ")

cleaned = ''.join(char.lower() for char in text if char.isalnum())
if cleaned == cleaned[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
