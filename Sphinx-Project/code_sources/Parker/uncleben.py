text = open("file_2.txt", "r")
words = 0
for line in text:
    line.split()
    for i in line.split():
        words += 1
        print (i)
print ("Количество слов: ", words)