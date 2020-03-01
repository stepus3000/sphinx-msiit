text = open("file_4.txt", "r")
text_2 = open("outfile_4.txt", "w")
for line in text:
    if line[1::] == " ":
            text_2.write(line)
    line.split()
    new_line = ' '.join(line.split())
    text_2.write(new_line)
    text_2.write("\n")
text_2.close()