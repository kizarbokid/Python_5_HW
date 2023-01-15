import random

def candy_game(candies):
    # Жеребьевка начального игрока
    current_player = random.randint(1, 2)
    print("Игрок", current_player, "начинает игру.")

    # Цикл обработки хода игрока
    max_turn=28
    while candies > 0:
        turn = int(input(f"Игрок {current_player},сколько конфет забираете (1-{max_turn})? "))
        turn = min(max_turn, turn,candies) # игрок не может взять более 28 конфет за раз или больше, чем осталось на столе
        candies -= turn
        print("Игрок", current_player, "взял",  turn, "конфет.")
        print("Осталось", candies, "конфет.")

        # Смена игроков после завершения хода
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

    # Определить победителя, когда конфеты закончились
    if current_player == 1:
        print("Игрок 2 выйграл!")
    else:
        print("Игрок 1 выйграл!")

candy_game(int(input("Сколько у вас конфет? ")))

