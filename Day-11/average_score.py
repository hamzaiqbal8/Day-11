"""Input a list of scores and return average rounded to 2 decimal places"""


scores_input = input("Enter scores separated by spaces: ")
scores = [float(score) for score in scores_input.split()]
average = sum(scores) / len(scores)

print("Average score:", round(average, 2))
