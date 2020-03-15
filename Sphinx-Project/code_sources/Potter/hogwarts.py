text = """ Внимание, внимание! 
Потерялась варежка. Цвет сине-желтый, возраст два года. 
Нашедшего  прошу  сообщить  по  телефону  223-322-223-322. \n \n \n"""
result = open ("outfile_2.txt", "w")
print ("Cколько раз хотите повторить текст?")
x = int(input())
result_text = text * x
result.write(result_text)
result.close()