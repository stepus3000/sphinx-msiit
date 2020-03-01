import random

for i in range(1 , 11):
   x = random.randint(-2, 2)
   y = random.randint(-2, 2)
   try:
       result = x / y
   except ZeroDivisionError:
       result = 0
   print(result)
  