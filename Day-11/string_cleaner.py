"""Remove punctuation, spaces, and convert string to lowercase"""

import string


text = input("Enter a string: ")


cleaned_text = ""

for char in text:
    if char.isalnum():
        cleaned_text += char.lower()


print("Cleaned string:", cleaned_text)
