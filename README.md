# 📊 GradeBook Analyzer

A simple and user-friendly Python application for analyzing student performance and generating detailed grade reports.

## 📝 Overview

GradeBook Analyzer is a command-line tool designed to help teachers quickly analyze student test results. Instead of manual calculations or complex spreadsheets, this program automates the entire process - from data entry to statistical analysis and grade distribution.

## ✨ Features

- **Easy Data Entry**: Simple prompts to enter student names and marks
- **Statistical Analysis**: Automatic calculation of averages, median, highest and lowest scores
- **Grade Assignment**: Automatic letter grade assignment (A, B, C, D, F)
- **Pass/Fail Analysis**: Identifies students who passed or failed (40 marks threshold)
- **Grade Distribution**: Shows how many students received each grade
- **Formatted Reports**: Clean, tabular display of all results
- **Interactive Menu**: User-friendly interface with re-run capability

## 🎯 Learning Objectives

This project demonstrates:
- Working with Python dictionaries and lists
- Implementing statistical functions (mean, median, min, max)
- Using control statements (if-elif-else)
- List comprehensions for data filtering
- Modular code design with functions
- String formatting with f-strings
- Input validation and error handling

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system
- Basic understanding of running Python scripts

### Installation

1. Download the `gradebook.py` file
2. Save it in a folder named `gradebook_analyzer`
3. No additional libraries required - uses only Python standard library!

### Running the Program

**On Windows:**
```bash
python gradebook.py
```

**On Mac/Linux:**
```bash
python3 gradebook.py
```

## 📖 How to Use

### Step 1: Start the Program
Run the script and you'll see a welcome message with a menu.

### Step 2: Enter Student Data
1. Choose Option 1 from the menu
2. Enter the number of students
3. For each student, provide:
   - Student name
   - Marks (0-100)

### Step 3: View Analysis
1. Choose Option 2 to see complete analysis including:
   - Class average and median
   - Top and lowest scorers
   - Grade distribution
   - Pass/fail summary
   - Individual student results table

### Step 4: Exit or Re-run
- Choose Option 3 to exit
- Or enter new data to analyze a different class

## 📊 Sample Output

```
=========================================================
           CLASS PERFORMANCE REPORT
=========================================================

Total Students: 5
Class Average: 76.40
Median Score: 78.00
Top Scorer: Prabhat Bhatia with 92.00 marks
Needs Improvement: Aradhya Mathur with 56.00 marks

---------------------------------------------------------
GRADE BREAKDOWN
---------------------------------------------------------
Grade A: 1 student(s) - 20.0% of class
Grade B: 1 student(s) - 20.0% of class
Grade C: 2 student(s) - 40.0% of class
Grade D: 1 student(s) - 20.0% of class
Grade F: 0 student(s) - 0.0% of class

---------------------------------------------------------
PASS/FAIL SUMMARY (Passing: 40 marks)
---------------------------------------------------------
✓ Passed: 5 student(s)
   Aayan Srivastwa, Aradhya Mathur, Prabhat Bhatia, Suhani Yadav, Kumar Partha

=========================================================
INDIVIDUAL STUDENT RESULTS
=========================================================
Name                 Marks        Grade      Result    
---------------------------------------------------------
Aayan Srivastwa      78.00        C          PASS      
Aradhya Mathur       56.00        F          FAIL      
Prabhat Bhatia       82.00        B          PASS      
Kumar Parhta         69.00        C          PASS      
Suhani Yadav         95.00        A          PASS      
=========================================================
```

## 📋 Grading Scale

| Grade | Marks Range |
|-------|-------------|
| A     | 90 - 100    |
| B     | 80 - 89     |
| C     | 70 - 79     |
| D     | 60 - 69     |
| F     | Below 60    |

**Passing Marks**: 40 and above

## 🛠️ Technical Details

### Functions Included

- `print_welcome()` - Displays welcome message
- `show_menu()` - Shows menu options
- `get_student_data()` - Handles data input with validation
- `calculate_average()` - Computes mean of marks
- `calculate_median()` - Finds median value
- `find_max_score()` - Identifies highest scorer
- `find_min_score()` - Identifies lowest scorer
- `assign_grade()` - Assigns letter grades
- `calculate_grade_distribution()` - Calculates grade counts
- `filter_pass_fail()` - Separates passed/failed students using list comprehension
- `display_statistics()` - Displays complete analysis report
- `main()` - Main program loop

### Data Structures

- **Marks Dictionary**: `{"StudentName": marks}`
- **Grades Dictionary**: `{"StudentName": "Grade"}`
- **Lists**: Used for passed and failed student names

## 🧪 Testing

Test the program with at least 5 students with varied marks:
- Some with marks > 90 (Grade A)
- Some between 60-89 (Grades B, C, D)
- Some below 40 (Failed students)
- Some below 60 but above 40 (Grade F but passed)

## ⚠️ Input Validation

The program includes validation for:
- Non-numeric inputs for student count and marks
- Marks outside 0-100 range
- Empty student names
- Invalid menu choices

## 🎓 Assignment Information

- **Course**: Programming for Problem Solving using Python
- **By**: Aayan Srivastwa

Date: November 05, 2025

---
