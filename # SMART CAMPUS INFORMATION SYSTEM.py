# SMART CAMPUS INFORMATION SYSTEM
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []
courses = []
# Student Registration & Grade Evaluation
def register_student():
    print("\n=== Student Registration ===")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    score = float(input("Enter exam score (0-100): "))

    if 90 <= score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    student = {"name": name,"age": age,"score": score,"grade": grade,"remark": remark}
    students.append(student)
    print("Name:", name) 
    print("Score:", score) 
    print("Grade:", grade) 
    print("Performance Remark:", remark) 

# Course Enrollment
def enroll_courses():
    print("\n=== Course Enrollment ===")
    max_courses = 5
    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")

        if course_name.lower() == "done":
            break

        credit = input("Enter credits: ")

        if not credit.isdigit():
            print("Invalid credit value!")
            continue

        credit = int(credit)

        if credit <= 0:
            print("Credits must be positive!")
            continue
        courses.append((course_name, credit))
        print("Course Added Successfully!")

    print("\nEnrolled Courses:")
    for c, cr in courses:
        print(f"{c} - {cr} Credits")

# Student Record Management
def display_students():
    students.append({"name": "Priya", "age": 20, "grades": [85, 90, 78]}) 
    students.append({"name": "Rahul", "age": 21, "grades": [72, 88, 91]}) 
    students.append({"name": "Anita", "age": 19, "grades": [95, 89, 92]}) 

    print("=== Student Records ===") 
    for student in students: 
        print("Name:", student["name"]) 
        print("Age:", student["age"]) 
        print("Grades:", student["grades"]) 

    event_A = {"Priya", "Rahul", "Anita", "Kiran"} 
    event_B = {"Rahul", "Anita", "Sneha"} 
 
    common_participants = event_A & event_B 
    all_participants = event_A | event_B 
    only_event_A = event_A - event_B 
 
    print("\n=== Event Participation Analysis ===") 
    print("Common Participants:", common_participants) 
    print("All Participants:", all_participants) 
    print("Only Event A Participants:", only_event_A)

# Sorting and Searching Student IDs
def sort_and_search():
    student_ids = [105, 102, 110, 108, 101, 115]
    print("\nOriginal IDs:", student_ids)
    # Bubble Sort
    n = len(student_ids)

    for i in range(n):
        for j in range(0, n-i-1):
            if student_ids[j] > student_ids[j+1]:
                student_ids[j], student_ids[j+1] = \
                    student_ids[j+1], student_ids[j]

    print("Sorted IDs:", student_ids)
    target = int(input("Enter ID to search: "))
    # Linear Search
    found = -1

    for i in range(len(student_ids)):
        if student_ids[i] == target:
            found = i
            break

    if found != -1:
        print("Linear Search: Found at index", found)
    else:
        print("Linear Search: Not Found")
    # Binary Search
    low = 0
    high = len(student_ids) - 1
    found = -1

    while low <= high:
        mid = (low + high) // 2

        if student_ids[mid] == target:
            found = mid
            break
        elif student_ids[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1

    if found != -1:
        print("Binary Search: Found at index", found)
    else:
        print("Binary Search: Not Found")

# Fee Calculation
def calculate_fee(tuition_fee, hostel_fee=0,
                  transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

def fee_management():
    print("\n=== Fee Calculation ===")

    tuition = float(input("Enter Tuition Fee: "))
    hostel = float(input("Enter Hostel Fee: "))
    transport = float(input("Enter Transport Fee: "))
    total = calculate_fee(tuition, hostel, transport)
    print("Total Fee =", total)

# File Handling
def file_management():
    print("\n=== File Management ===")

    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print("File created successfully.")

    with open("student_records.txt", "r") as file:
        records = file.readlines()
    print("\nContents of File:")
    for record in records:
        print(record.strip())

    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        name = parts[1]
        marks = int(parts[2])
        total_students += 1
        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    average = total_marks / total_students

    print("\nReport")
    print("Total Students:", total_students)
    print("Average Marks:", average)
    print("Top Student:", top_student)

# Directory Scanning
class MissingFileOrFolderError(Exception):
    pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("Invalid Path")
        print("\nDirectory Structure:\n")

        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = " " * 4 * (level + 1)

            for f in files:
                print(f"{subindent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty Folder: {root}")  
                                  
    except FileNotFoundError as e:
        print(e)

    except MissingFileOrFolderError as e:
        print(e)

    except Exception as e:
        print(e)

def directory_management():
    path = input("Enter Directory Path: ")
    scan_directory(path)

# Student Performance Analyser Using NumPy,Pandas and Matplotlib
def performance_analysis():
    print("\n=== Performance Analytics ===")
    data = {"Name": ["Arjun", "Meera", "Ravi", "Anita"],
        "Math": [85, 92, 76, 89],
        "Science": [80, 95, 78, 88],
        "English": [82, 90, 75, 91]}
    
    df = pd.DataFrame(data)
    print("\nRaw Data")
    print(df)
    print("\nStatistical Summary")
    print(df.describe())

    scores = df[["Math", "Science", "English"]].to_numpy()

    mean_scores = np.mean(scores, axis=0)
    median_scores = np.median(scores, axis=0)
    std_scores = np.std(scores, axis=0)

    print("\nMean Scores:", mean_scores)
    print("Median Scores:", median_scores)
    print("Standard Deviation:",std_scores)

    print("\nTop Performers")
    print("Math:",
          df.loc[df["Math"].idxmax(), "Name"])

    print("Science:",
          df.loc[df["Science"].idxmax(), "Name"])

    print("English:",
          df.loc[df["English"].idxmax(), "Name"])

    subjects = ["Math", "Science", "English"]

    plt.figure(figsize=(6, 4))
    plt.bar(subjects, mean_scores)
    plt.title("Average Scores")
    plt.show()

    df.plot(x="Name",
        y=["Math", "Science", "English"],
        kind="bar")
    plt.title("Student Performance")
    plt.show()

#---------------------------------------------------
# MAIN MENU
def main():
    while True:

        print("\n")
        print("================================")
        print(" SMART CAMPUS INFORMATION SYSTEM")
        print("================================")
        print("1. Student Registration")
        print("2. Course Enrollment")
        print("3. Student Records")
        print("4. Sorting & Searching")
        print("5. Fee Calculation")
        print("6. File Management")
        print("7. Directory Scanning")
        print("8. Performance Analytics")
        print("9. Exit")
        choice = input("Enter Choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            enroll_courses()
        elif choice == "3":
            display_students()
        elif choice == "4":
            sort_and_search()
        elif choice == "5":
            fee_management()
        elif choice == "6":
            file_management()
        elif choice == "7":
            directory_management()
        elif choice == "8":
            performance_analysis()
        elif choice == "9":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    main()