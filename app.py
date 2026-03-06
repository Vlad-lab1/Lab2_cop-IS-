import random

def check_guess(secret, guess):
    if guess < secret:
        return "more"
    elif guess > secret:
        return "less"
    else:
        return "correct"


def play_game():
    number = random.randint(0, 1000)
    guess = -1
    attempts = 0

    print("Гра: Вгадай число від 0 до 1000")

    while guess != number:
        guess = int(input("Введіть число: "))
        attempts += 1

        result = check_guess(number, guess)

        if result == "more":
            print("Загадане число більше")
        elif result == "less":
            print("Загадане число менше")
        else:
            print("Вітаю! Ви вгадали число.")
            print("Кількість спроб:", attempts)

if name == "main":
    play_game()
