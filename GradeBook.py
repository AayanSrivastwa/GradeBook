# GradeBook Analyzer Program
# Name: Aayan Srivastwa
# Date: 5 Nov 2025
# This program helps to enter student marks and analyze their grades.

from statistics import median

# --- Function to calculate average marks ---
def calculate_average(marks):
    total = sum(marks.values())
    count = len(marks)
    avg = total / count
    return avg

# --- Function to find median ---
def calculate_median(marks):
    return median(marks.values())

# --- Function to find highest scorer ---
def find_highest(marks):
    name = max(marks, key=marks.get)
    return name, marks[name]

# --- Function to find lowest scorer ---
def find_lowest(marks):
    name = min(marks, key=marks.get)
    return name, marks[name]

# --- Function to assign grades ---
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

# --- Main program starts here ---
print("Welcome to the GradeBook Analyzer!")

# Asking how many students
n = int(input("Enter number of students: "))

# Taking names and marks
marks = {}
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    marks[name] = mark

# --- Calculations ---
avg = calculate_average(marks)
med = calculate_median(marks)
high_name, high_score = find_highest(marks)
low_name, low_score = find_lowest(marks)

# --- Assign grades ---
grades = {}
for name, mark in marks.items():
    grades[name] = assign_grade(mark)

# --- Count grade distribution ---
grade_count = {"A":0, "B":0, "C":0, "D":0, "F":0}
for g in grades.values():
    grade_count[g] += 1

# --- Pass / Fail using list comprehension ---
passed = [name for name, mark in marks.items() if mark >= 40]
failed = [name for name, mark in marks.items() if mark < 40]

# --- Display Results ---
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
