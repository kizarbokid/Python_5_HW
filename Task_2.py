
# Печать поля с разделителем |
def print_board():
    for row in field:
        print("|".join(row))

# Проверка победителя (возвращает ЛОЖЬ если ни одно из условий не сработало)
def check_win(player):
    for i in range(3):
        # горизонтально по строкам
        if field[i][0] == player and field[i][1] == player and field[i][2] == player:
            return True
        # вертикально по столбцам
        if field[0][i] == player and field[1][i] == player and field[2][i] == player:
            return True
    # Диагонали
    if field[0][0] == player and field[1][1] == player and field[2][2] == player:
        return True
    if field[0][2] == player and field[1][1] == player and field[2][0] == player:
        return True
    return False

# Проверка поля на наличие пустых ячеек
def is_available(field):
    for i in range(3):
        for j in range(3):
            if field[i][j]==' ':
                return True        
    return False

# Создание пустого игрового поля
field = [[' ' for _ in range(3)] for _ in range(3)]

current_player = 'X'

# Игра будет продолжаться, пока есть свободные клетки
while is_available(field):
    print_board()
    print("Ход игрока", current_player,",")
    row = int(input("Введите строку (0-2): "))
    col = int(input("Введите столбец (0-2): "))

    if field[row][col] != ' ':
        print("Недопустимый ход, клетка занята!")
        continue
    
    field[row][col] = current_player

    if check_win(current_player):
        print("Игрок", current_player, "выйграл!")
        break

    # Смена игроков
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
else:
    print("Ничья!")