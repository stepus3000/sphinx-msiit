text = open("file_2.txt", "r")
letters = 0
words = 0
for line in text:
    line.split()
    for i in line.split():
        words += 1
    new_line = ''.join(line.split())
    letters += len(new_line)
print ("Количество букв: ", letters)
print ("Количество слов: ", words)