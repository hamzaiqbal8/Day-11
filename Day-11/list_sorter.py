"""list_sorter.py"""

user_input = input("Enter numbers separated by commas: ")
num_list = [int(x) for x in user_input.split(',')]

for i in range(len(num_list)):
    for j in range(0, len(num_list) - i - 1):
        if num_list[j] > num_list[j + 1]:
            # Swap
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print("Sorted List:", num_list)
