word = []
for i in range(5):
    word.append(input())
result = []
for a in range(5):
    try:
        result.append(int(word[a]))
    except ValueError:
        continue
print(result)
if len(result) == len(word):
    print('Все зашибишь, все элементы прошли проврку, красава')