# Students List
students = [
    ['Amal', 95],
    ['Danah', 60],
    ['Eman', 90],
    ['Haneen', 97],
    ['Kholud', 64]
]

# Start Of Code.
print('\t\tStudents Grades')
print('*' * 31)
print("Name\t\tGrade\t\tDegree")
for name, grade in students:

    if grade >= 95:
        degree = "A+"
    elif grade >= 90 or grade == 94:
        degree = "A"
    elif grade >= 85 or grade == 89:
        degree = "B+"
    elif grade >= 80 or grade == 84:
        degree = "B"
    elif grade >= 75 or grade == 79:
        degree = "C+"
    elif grade >= 70 or grade == 74:
        degree = "C"
    elif grade >= 65 or grade == 69:
        degree = "D+"
    elif grade >= 60 or grade == 64:
        degree = "D"
    else:
        degree = "F"

    # Printing Result
    print(f"{name} \t|\t {grade} \t|\t {degree}")


"""# The Highest && Lowest Grade At Grades.
grades = [column[1] for column in students]

highestGrade = max(grades)
lowestGrade = min(grades)

print(f'\nHighest Grade: {highestGrade}\nLowest Grade: {lowestGrade}\n')
"""
