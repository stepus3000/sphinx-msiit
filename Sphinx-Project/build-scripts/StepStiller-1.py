import os     # two empty lines after imports


directory = '../code_sources'
files = os.listdir(directory)
print(files)
print(type(files))

for file in files:
    with open(file + '.rst', 'w') as next_file:
       pass


def make_dict(directory):
    dictionary = dict()
    for key in files:
        directory_plus = f"{directory}/{key}"
        value = os.listdir(directory_plus)
        dictionary[key] = value
    print(dictionary)
    write_in(dictionary)
    write_in_plus()
       

  


def write_in(dictionary):
    fil = os.listdir(directory)
    print(fil)
    print('---------------')
    for file in files:
        with open(f"{file}.rst", 'a') as next_file:
            next_file.write(file)
            next_file.write('''
========================
''')


def write_in_plus():
    elements = []
    for one in files:
        directory_plus = f"{directory}/{one}"
        elements.append(os.listdir(directory_plus))
    print(elements)
make_dict(directory)