# Student Grade Calculator
# This program calculates student averages, letter grades,
# the top performer, and overall class statistics.

# Store student names and their grades in a dictionary
student_grades = {
    "Maya": [88, 92, 84],
    "Jordan": [95, 90, 93],
    "Carlos": [72, 68, 75],
    "Noah": [58, 64, 55]
}

# Calculate each student's average grade
student_averages = {}

for student_name, grade_list in student_grades.items():
    average_score = sum(grade_list) / len(grade_list)
    student_averages[student_name] = average_score


# Determine each student's letter grade
student_letter_grades = {}

for student_name, average_score in student_averages.items():

    if average_score >= 90:
        letter_grade = "A"

    elif average_score >= 80:
        letter_grade = "B"

    elif average_score >= 70:
        letter_grade = "C"

    elif average_score >= 60:
        letter_grade = "D"

    else:
        letter_grade = "F"

    student_letter_grades[student_name] = letter_grade


# Find the student with the highest average
top_student = ""
highest_average = -1

for student_name, average_score in student_averages.items():

    if average_score > highest_average:
        highest_average = average_score
        top_student = student_name


# Calculate the overall class average
class_average = sum(student_averages.values()) / len(student_averages)


# Count how many students passed with a C or better
passing_count = 0

for letter_grade in student_letter_grades.values():

    if letter_grade in ["A", "B", "C"]:
        passing_count += 1


# Display the results
print("STUDENT GRADE REPORT")
print("------------------------------")

for student_name in student_grades:
    print(
        f"{student_name}: "
        f"Average = {student_averages[student_name]:.2f}, "
        f"Letter Grade = {student_letter_grades[student_name]}"
    )

print("------------------------------")
print(f"Top Performer: {top_student}")
print(f"Top Average: {highest_average:.2f}")
print(f"Overall Class Average: {class_average:.2f}")
print(f"Students Passed: {passing_count} out of {len(student_grades)}")