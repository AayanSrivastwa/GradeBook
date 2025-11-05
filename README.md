Name: Aayan Srivastwa

Course: Programming for Problem Solving using Python
Date: 5 November 2025

Assignment No.: 2

Topic: GradeBook Analyzer

🔹 Aim

To write a Python program that helps a teacher record and analyze student marks by calculating average, median, highest, and lowest marks, assigning grades, and showing pass/fail lists.

🔹 Objectives

Input student names and marks.

Calculate average, median, highest, and lowest marks.

Assign grades automatically using conditions.

Count how many students fall in each grade category.

Separate pass and fail students using list comprehension.

Display a well-formatted report of all students.

🔹 Algorithm

Start the program.

Ask the user for the number of students.

Take each student’s name and marks as input.

Store names and marks in a dictionary.

Use functions to calculate:

Average marks

Median marks

Highest and lowest marks

Assign grades using conditional statements:

A → 90 and above

B → 80–89

C → 70–79

D → 60–69

F → below 60

Count how many students got each grade.

Create two separate lists using list comprehension: one for passed students (≥40) and one for failed students (<40).

Display all results in a clear tabular format.

End the program.

🔹 Program Code
# GradeBook Analyzer Program
# Name: Aayan Srivastwa
# Date: 5 Nov 2025

from statistics import median

# Function to calculate average
def calculate_average(marks):
    total = sum(marks.values())
    count = len(marks)
    avg = total / count
    return avg

# Function to find median
def calculate_median(marks):
    return median(marks.values())

# Function to find highest marks
def find_highest(marks):
    name = max(marks, key=marks.get)
    return name, marks[name]

# Function to find lowest marks
def find_lowest(marks):
    name = min(marks, key=marks.get)
    return name, marks[name]

# Function to assign grades
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Main program
print("Welcome to the GradeBook Analyzer!")
n = int(input("Enter number of students: "))

marks = {}
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    marks[name] = mark

# Calculations
avg = calculate_average(marks)
med = calculate_median(marks)
high_name, high_score = find_highest(marks)
low_name, low_score = find_lowest(marks)

# Assign grades
grades = {}
for name, mark in marks.items():
    grades[name] = assign_grade(mark)

# Grade count
grade_count = {"A":0, "B":0, "C":0, "D":0, "F":0}
for g in grades.values():
    grade_count[g] += 1

# Pass / Fail using list comprehension
passed = [name for name, mark in marks.items() if mark >= 40]
failed = [name for name, mark in marks.items() if mark < 40]

# Display Results
print("\n===== GradeBook Report =====")
print(f"Total Students: {len(marks)}")
print(f"Average Marks : {avg:.2f}")
print(f"Median Marks  : {med}")
print(f"Highest Marks : {high_score} ({high_name})")
print(f"Lowest Marks  : {low_score} ({low_name})")

print("\nGrade Distribution:")
for g, c in grade_count.items():
    print(f"Grade {g}: {c} student(s)")

print("\nPass List:", passed)
print("Fail List:", failed)

print("\nName\tMarks\tGrade")
print("------------------------")
for name, mark in marks.items():
    print(f"{name}\t{mark}\t{grades[name]}")
print("------------------------")
print("Analysis Completed Successfully!")

🔹 Sample Output
Welcome to the GradeBook Analyzer!
Enter number of students: 5
Enter name of student 1: Aisha
Enter marks of Aisha: 85
Enter name of student 2: Rohan
Enter marks of Rohan: 67
Enter name of student 3: Meena
Enter marks of Meena: 92
Enter name of student 4: Arjun
Enter marks of Arjun: 54
Enter name of student 5: Tara
Enter marks of Tara: 38

===== GradeBook Report =====
Total Students: 5
Average Marks : 67.20
Median Marks  : 67.0
Highest Marks : 92.0 (Meena)
Lowest Marks  : 38.0 (Tara)

Grade Distribution:
Grade A: 1 student(s)
Grade B: 1 student(s)
Grade C: 0 student(s)
Grade D: 1 student(s)
Grade F: 2 student(s)

Pass List: ['Aisha', 'Rohan', 'Meena', 'Arjun']
Fail List: ['Tara']

Name    Marks   Grade
------------------------
Aisha   85.0    B
Rohan   67.0    D
Meena   92.0    A
Arjun   54.0    F
Tara    38.0    F
------------------------
Analysis Completed Successfully!

🔹 Output Screenshot (optional)

(Paste a screenshot of your Python terminal output here if required in your report.)

🔹 Result / Conclusion

The Python program for the GradeBook Analyzer was successfully executed.
It allows the user to input student data and automatically computes the average, median, highest, and lowest marks.
It correctly assigns grades, counts the number of students in each grade, and separates the pass/fail list using list comprehension.
The results are displayed clearly in a tabular format.
Hence, the experiment is successfully verified.
