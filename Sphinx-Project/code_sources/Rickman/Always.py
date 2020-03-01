text = open ("file_5.txt", "r")
text_2 = open ("outfile_5.txt", "w")
dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'F', 'а':'f', 'Б':'<', 'б':',', 'В':'D', 'в':'d',
       'Г':'U', 'г':'u', 'Д':'L', 'д':'l', 'Е':'T', 'е':'t', 'Ё':'~', 'ё':'`', 'Ж':':', 'ж':';',
       'З':'P', 'з':'p', 'И':'B', 'и':'b', 'Й':'Q', 'й':'q', 'К':'R', 'к':'r', 'Л':'K', 'л':'k',
       'М':'V', 'м':'v', 'Н':'Y', 'н':'y', 'О':'J', 'о':'j', 'П':'G', 'п':'g', 'Р':'H', 'р':'h', 
       'С':'C', 'с':'c', 'Т':'N', 'т':'n', 'У':'E', 'у':'e', 'Ф':'A', 'ф':'a', 'Х':'{', 'х':'[',
       'Ц':'W', 'ц':'w', 'Ч':'X', 'ч':'x', 'Ш':'I', 'ш':'i', 'Щ':'O', 'щ':'o', 'Ы':'S',
       'ы':'s', 'Э':'Э', 'э':'э', 'Ю':'>', 'ю':'.', 'Я':'Z', 'я':'z',

       'F':'А', 'f':'а', '<':'Б', ',':'б', 'D':'В', 'd':'в',
       'U':'Г', 'u':'г', 'L':'Д', 'l':'д', 'T':'Е', 't':'е', '~':'Ё', '`':'ё', ':':'Ж', ';':'ж',
       'P':'З', 'p':'з', 'B':'И', 'b':'и', 'Q':'Й', 'q':'й', 'R':'К', 'r':'к', 'K':'K', 'k':'л',
       'V':'М', 'v':'м', 'Y':'Н', 'y':'н', 'J':'O', 'j':'о', 'G':'П', 'g':'п', 'H':'Р', 'h':'р', 
       'C':'С', 'c':'с', 'N':'Т', 'n':'т', 'E':'У', 'e':'у', 'A':'Ф', 'a':'ф', '{':'Х', '[':'х',
       'W':'Ц', 'w':'ц', 'X':'Ч', 'x':'ч', 'I':'ш', 'i':'ш', 'O':'Щ', 'o':'щ', 'S':'Ы',
       's':'ы', '>':'Ю', '.':'ю', 'Z':'Я', 'z':'я'}
s = str()
ans = []
for line in text:
    for i in line:
            if i in dic:
                s = dic[i]
            else:
                s = i
            ans.append(s)

result = ''.join(ans)
text_2.write(result)
text_2.close()