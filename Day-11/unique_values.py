"""unique_values.py"""

user_input = input("Enter items separated by commas: ")
input_list = user_input.split(',')


unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

print("List with unique values:", unique_list)
