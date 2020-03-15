import random


error = ["Я не понимаю, введи цифрой.", "Не смешно, давай нормально.", "Очень смешно", "Так трудно ввести пару цифр?", "Неправильный ответ, давай еще раз."]
while True:
    year = input("Сколько тебе лет? ")
    try:
        answer = int(year)
        if 0 <= answer <= 140:
            print("Крутяк!")
            break
        elif answer < 0:
            print("Да ладно, ты не можешь быть младше новорденного.")
        elif answer > 140:
            print("Давай честно, я не верю, что это твой возраст")
    except ValueError:
        print(random.choice(error))
    