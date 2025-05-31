"""File: student_report_card.py"""


name = input("Enter student name: ")


subjects = []
marks = []


for i in range(3):
    subject = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    subjects.append(subject)
    marks.append(mark)


total = sum(marks)
percentage = total / 3


if percentage >= 80:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
else:
    grade = 'C'


print("\n--- Report Card ---")
print("Name:", name)
for i in range(3):
    print(f"{subjects[i]}: {marks[i]} / 100")
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
