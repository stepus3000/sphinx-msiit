with open('file.txt', 'r') as intput, open('outfile.txt', 'w') as output:
    for line in intput:
        if line.strip():
            output.write(line)
intput.close()
output.close()