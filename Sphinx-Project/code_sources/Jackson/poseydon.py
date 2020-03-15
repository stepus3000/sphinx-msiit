numbers = []
counter = 5
while True: 
    if counter == 0:
                print(numbers) 
                break 
    for i in range(5):
        number = input("Введи число:  ")
        try:
            answer = int(number)
            numbers.append(number)
            counter -= 1
            if counter == 0:
                break 
        except ValueError:
            print("Ты чето попутал, просто введи число")
            continue