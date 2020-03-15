"""
Этот модуль автоматизирует создание файлов с расширением '.rst',
а также написание sphinx-разметки для создания html-документа. 
"""
import os


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

    :param dictionary: dictionary in which keys it is names students and values it is works students.
    :param target_path: the path where notebooks are created to create html pages.
    :type dictionary: dict
    :type target_path: str  
    """
    for student in dictionary:  # for each student (key in dictionary)
        with open(f"{target_path}/{student}.rst", 'a') as next_file:  # open file with student name in writing mode
            # write to file student files. hint: files are in dictionary[student] 
            next_file.write(student)
            next_file.write('\n')
            next_file.write('=' * len(student))
            next_file.write('\n')  # write header de des
            works = (dictionary[student])
            for file in works:
                    with open('build-scripts/example.txt', 'r') as do_it:
                        for line in do_it:
                            next_file.write(line.format(student = student, file = file))
                    do_it.close()
    
def make_maine_page(dictionary, target_path):
    """
    Сreates links to pages with student works on the main pages.

    :param dictionary: dictionary in which keys it is names students and values it is works students.
    :param target_path: the path where notebooks are created to create html pages.
    :type dictionary: dict
    :type target_path: str
    """
    line_list = []
    with open('build-scripts/index.txt', 'r') as index_list:
        for line in index_list:
            line_list.append(line)
            if line == '   :maxdepth: 2\n':
                line_list.append('\n')
                for student in dictionary:
                    line_list.append(f' solutions/{student}\n')
    with open('sphinx-files/index.rst', 'w') as index_list:
        for result in line_list:
            index_list.write(result)
        

directory = 'code_sources'
students_dict = make_dict(directory)
make_student_page(students_dict, "sphinx-files/solutions")
make_maine_page(students_dict, "sphinx-files/solutions")