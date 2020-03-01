'''
it class to be
'''

import os     # two empty lines after import


def make_dict(directory):
    """
    Makes dictionary with students files.
    
    Uses student name as a key and list of students files as a value.
    
    :param directory: path to sources (studens folders).
    :type directory: str
    :return: dictionary with names of students files.
    :rtype: dict
    """
    students = os.listdir(directory)
    dictionary = dict()
    for student in students:
        student_directory = f"{directory}/{student}"
        student_files = os.listdir(student_directory)
        dictionary[student] = student_files
    return dictionary


def make_student_page(dictionary, target_path):
    """
    Сreates notebooks with students' works for creating html pages.
    """
    for student in dictionary:  # for each student (key in dictionary)
        with open(f"{target_path}/{student}.rst", 'a') as next_file:  # open file with student name in writing mode
            # write to file student files. hint: files are in dictionary[student]
            next_file.write(student)
            next_file.write('\n')
            next_file.write('=' * len(student))
            next_file.write('\n')  # write header
            works = (dictionary[student])
            for file in works:
                    next_file.write(':download:`')
                    next_file.write(file)
                    next_file.write(' <../../code_sources/')
                    next_file.write(student)
                    next_file.write('/')
                    next_file.write(file)
                    next_file.write('>`')  # write students` works in notebooks
                    next_file.write('\n')
                    next_file.write('\n')
                    next_file.write('.. literalinclude:: ../../code_sources/')
                    next_file.write(student)
                    next_file.write('/')
                    next_file.write(file)
                    next_file.write('\n')
                    next_file.write('  :language: python')
                    next_file.write('\n')
                    next_file.write('  :linenos:')
                    next_file.write('\n')
                    next_file.write('\n')



directory = 'code_sources'
students_dict = make_dict(directory)
make_student_page(students_dict, "sphinx-files/solutions")