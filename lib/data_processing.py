# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    # Unpacking the tuple into variables
    student_id, name, major = student

    # Returning formatted string
    return f"ID: {student_id} | Name: {name} | Major: {major}"

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    # Looping through each student
    for student in student_list:
        # Printing formatted student info
        print(format_student_data(student))