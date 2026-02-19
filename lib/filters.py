# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    # Converting the given major to lowercase so comparison is not case sensitive
    major = major.lower()

    # Using list comprehension to filter students
    filtered_students = [
        student for student in student_list
        if student[2].lower() == major
    ]

    return filtered_students
