import random
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Крестики-нолики")
for i in range(3):
    print(" # " + str(l[i][0]) + " # " + str(l[i][1]) + " # " + str(l[i][2]) + " #")
n = random.randint(1, 2)
if n == 1:
    flag = True
else:
    flag = False
if flag:
    print("Первый ход делает: X")
    step = "X"
else:
    print("Первый ход делает: O")
    step = "O"


def check_win(l, count_step):
    win_or_not = False
    if l[0][0] == l[0][1] == l[0][2]:
        win_or_not = True
    elif l[1][0] == l[1][1] == l[1][2]:
        win_or_not = True
    elif l[2][0] == l[2][1] == l[2][2]:
        win_or_not = True

    elif l[0][0] == l[1][0] == l[2][0]:
        win_or_not = True
    elif l[0][1] == l[1][1] == l[2][1]:
        win_or_not = True
    elif l[0][2] == l[1][2] == l[2][2]:
        win_or_not = True

    elif l[0][0] == l[1][1] == l[2][2]:
        win_or_not = True
    elif l[0][2] == l[1][1] == l[2][0]:
        win_or_not = True

    if win_or_not:
        return 1
    else:
        if count_step == 9:
            return 2
        else:
            return 0


count_step = 0


def pole(l, xy, step):
    if xy in [1, 2, 3]:
        l[0][xy - 1] = step
    elif xy in [4, 5, 6]:
        l[1][xy - 4] = step
    elif xy in [7, 8, 9]:
        l[2][xy - 7] = step
    return l


while True:
    xy = input()
    if xy not in ["1", "2", '3', '4', '5', '6', '7', '8', '9']:
        print("Неверный ход")
        continue
    xy = int(xy)
    count_step += 1
    pole(l, xy, step)
    for i in range(3):
        print(" # " + str(l[i][0]) + " # " + str(l[i][1]) + " # " + str(l[i][2]) + " #")

    win = check_win(l, count_step)
    if win == 1:
        print("Победа игрока:", step)
        break
    elif win == 2:
        print("Ничья")
        break
    if flag:
        step = "O"
        flag = False
    else:
        step = "X"
        flag = True

    print("Ход игрока", step)