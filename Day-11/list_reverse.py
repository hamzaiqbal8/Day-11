"""list_reverse.py"""
user_input = input("Enter elements separated by commas: ")
original_list = user_input.split(',')

reversed_list = []
for i in range(len(original_list) - 1, -1, -1):
    reversed_list.append(original_list[i])

print("Reversed List:", reversed_list)
