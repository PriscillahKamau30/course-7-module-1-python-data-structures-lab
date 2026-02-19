# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # Using set comprehension to collect all majors
    majors = {student[2] for student in student_list}


    # Returning the set (this was likely missing)
    return majors
