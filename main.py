field_play = [
    ['-']*3
    for i in range(3)
]

def draw_field_play(field_play): #рисуем игровое поле
    print("  0 1 2")
    for i in range(len(field_play)):
        print(str(i), *field_play[i])

def moves(field_play, user): #прописываем ходы
    while True:
        move = list(map(int, (input(f"Введите координаты {user} типа INT (через пробел):").split())))
        if len(move) != 2:
            print("Введите две координаты!")
            continue
        x, y = move
        if x not in [0, 1, 2]:
            print("Неверные координаты для ПЕРВОГО значения!")
            continue
        if y not in [0, 1, 2]:
            print("Неверные координаты для ВТОРОГО значения!")
            continue
        if field_play[x][y] != '-':
            print("Клетка занята!\n"
                  "Найдите пустое поле")
            continue
        break
    return x, y

def rules(field_play, user): #выигрышные линии
    win_lines = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2))
    )
    for lines in win_lines:
        symbols = []
        for c in lines:
            symbols.append(field_play[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

def game():
    print("---Добро пожаловать в игру!---")
    count = 0
    while True:
        if count % 2 == 0:
            user = "X"
        else:
            user = "0"
        draw_field_play(field_play)
        if count < 9:
            x, y = moves(field_play, user)
            field_play[x][y] = user
        if count == 9:
            print("Ничья!\n---Конец игры---")
            break
        if rules(field_play, user):
            print(f"Выйграл {user}\n---Конец игры---")
            break
        count += 1

game() #запуск игры




