def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

average = calculate_average(marks1, marks2, marks3)
grade = calculate_grade(average)

print("Average:", average)
print("Grade:", grade)
