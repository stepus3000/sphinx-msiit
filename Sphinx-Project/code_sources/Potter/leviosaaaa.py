with open('file_3.txt', 'r') as text, open('outfile_3.txt', 'a') as new_text:
 for line in text:
    new_line = line.replace('ё', 'е')
    print (line)
    print (new_line)
    new_text.write(new_line)
new_text.close()