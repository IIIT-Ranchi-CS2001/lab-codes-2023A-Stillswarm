
"""
    Enter the following details of a student: Name, Roll No, and marks in Mathematics examination out of 100.
    Write a Python script to display student details.
"""
name, rollno_str, marks_str = input("Enter the name, roll no., marks: ").split()

rollno = int(rollno_str)
marks = int(marks_str)
gradePoints = 0
remarks = ""

if marks >= 90:
    gradePoints = 10
    remarks = "OUTSTANDING"
elif marks >= 80:
    gradePoints = 9
    remarks = "VERY GOOD"
elif marks >= 70:
    gradePoints = 8
    remarks = "GOOD"
elif marks >= 60:
    gradePoints = 7
    remarks = "AVERAGE"
elif marks >= 50:
    gradePoints = 6
    remarks = "PASS"
else:
    gradePoints = 0
    remarks = "FAIL"

print("Name: ", name)
print("Roll No: ", rollno)
print("Marks: ", marks)
print("Grade Points: ", gradePoints)
print("Remarks: ", remarks)