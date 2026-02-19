# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
     # Making comparison case insensitive
    major = major.lower()

    # Returning a generator expression
    return (
        student for student in student_list
        if student[2].lower() == major
    )
