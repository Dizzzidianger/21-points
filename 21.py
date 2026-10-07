# игра 21 очко

import random


# ===== КЛАССЫ =====

class Enemy:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.name} ({self.difficulty})"


class Bot:
    def __init__(self, name, min_score, max_score):
        self.name = name
        self.min_score = min_score
        self.max_score = max_score

    def get_score(self):
        return random.randint(self.min_score, self.max_score)


# ===== ФУНКЦИЯ СТАРТА =====

def show_menu():
    while True:
        print("\nДобро пожаловать в игру - 21 очко")
        print("Выберите:")
        print("1) Старт")
        print("2) Выход")

        try:
            b = int(input("Ваш выбор: "))
            if b == 1:
                return True
            elif b == 2:
                print("Всего доброго!")
                return False
            else:
                print("Ошибка: введите 1 или 2")
        except ValueError:
            print("Ошибка: введите число")


# ===== ФУНКЦИЯ ВЫБОРА ПРОТИВНИКА =====

def choose_enemy():
    enemy_1 = Enemy("Мария", "Легкая")
    enemy_2 = Enemy("Боря", "Средняя")
    enemy_3 = Enemy("Свин", "Шулер")

    print("\nВыберите противника:")
    print(f"1) {enemy_1}")
    print(f"2) {enemy_2}")
    print(f"3) {enemy_3}")

    try:
        answer = int(input("Ваш выбор: "))
        if answer in [1, 2, 3]:
            return answer
        else:
            print("Неверный выбор")
            return 0
    except ValueError:
        print("Ошибка: введите число")
        return 0


# ===== ФУНКЦИЯ ПОЛУЧЕНИЯ БОТА =====

def get_bot(choice):
    if choice == 1:
        return Bot("Мария", 1, 15)
    elif choice == 2:
        return Bot("Боря", 5, 18)
    elif choice == 3:
        return Bot("Свин", 10, 21)
    else:
        return None


# ===== ФУНКЦИЯ ИГРЫ =====

def game(bot):
    total_user = 0
    total_bot = 0

    print(f"\nВы выбрали противника: {bot.name}")
    print("Цель: набрать больше очков, чем бот, но не больше 21")

    while True:
        print(f"\nВаш счёт: {total_user}")
        print("Ваши действия?")
        print("1) Взять карту")
        print("2) Оставить")

        try:
            answer = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите число")
            continue

        if answer == 1:
            card = random.randint(1, 11)
            total_user += card
            print(f"Вы взяли карту: {card}")

            if total_user > 21:
                print(f"Перебор! Ваш счёт: {total_user}")
                break

        elif answer == 2:
            print("Вы остановились")
            break

        else:
            print("Неверное действие")

    # Ход бота
    total_bot = bot.get_score()
    print(f"\n{bot.name} набрал: {total_bot}")

    # Подсчёт очков
    print("\n===== РЕЗУЛЬТАТ =====")
    print(f"Вы: {total_user}")
    print(f"{bot.name}: {total_bot}")

    if total_user > 21:
        print("Вы проиграли (перебор)")
    elif total_bot > 21:
        print("Вы выиграли! (у бота перебор)")
    elif total_user > total_bot:
        print("Вы выиграли!")
    elif total_user < total_bot:
        print("Вы проиграли")
    else:
        print("Ничья")


# ===== ОСНОВНАЯ ПРОГРАММА =====

def main():
    while True:
        if not show_menu():
            break

        enemy_choice = choose_enemy()
        if enemy_choice == 0:
            continue

        bot = get_bot(enemy_choice)
        if bot is None:
            continue

        game(bot)

        again = input("\nСыграть ещё? (да/нет): ").lower()
        if again != "да":
            print("Всего доброго!")
            break


main()