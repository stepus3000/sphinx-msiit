import os



directory = '../code_sources'
files = os.listdir(directory)
print(files)




print(type(files))
for file in files:
    with open(file + '.rst', 'w') as next_file:
       pass
    

def m make_dictionary():
       dictionary = dict()
       for Key in files:
              directory_plus = '../code_sources/' + Key
              Value = os.listdir(directory_plus)
              dictionary[Key] = Value
       print(dictionary)
       page(dictionary)
       

  


def page(dictionary):
       fil = os.listdir(directory)
       print(fil)
       print('---------------')
       for file in files:
              with open(file + '.rst', 'a') as next_file:
                     next_file.write(file)
                     next_file.write('''
========================
''') 
                     for element in dict.values(dictionary):
                            with open(file + '.rst', 'a') as next_file:
                                  print (element)


diction()