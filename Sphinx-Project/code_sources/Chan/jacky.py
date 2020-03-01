first =  ['goodmorning', 'bye', 'hello']
secend = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
third =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
four =   ['boll', 'doll', 'monkey', 'world']
five =   ['only one']

try:
    for i in range(0 , 10):
        print(first[i])
except IndexError:
    print('Здесь только ', i, ' элемента(ов)')

print('\n')

try:
    for i in range(0 , 10):
        print(secend[i])
        
except IndexError:
    print('Здесь только ', i, ' элемента(ов)')

print('\n')

try:
    for i in range(0 , 10):
        print(third[i])
except IndexError:
    print('Здесь только ', i, ' элемента(ов)')

print('\n')

try:
    for i in range(0 , 10):
        print(four[i])
except IndexError:
    print('Здесь только ', i, ' элемента(ов)')

print('\n')

try:
    for i in range(0 , 10):
        print(five[i])      
except IndexError:
    print('Здесь только ', i, ' элемент')