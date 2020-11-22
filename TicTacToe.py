# write your code here
def wincheck(line):     # checking status of current game
    wc = 0
    sp = 0
    for i in range(0, 8):
        if line[i].count("X") == 3:
            winner = "X"
            wc = wc + 1
        elif line[i].count("O") == 3:
            winner = "O"
            wc = wc + 1
        sp = sp + line[i].count("_")
    if wc == 1:
        return ' '.join([winner, "wins"])
    elif wc == 0 and sp == 0:
        return str("Draw")
    elif wc == 0 and sp > 0:
        return str("Game not finished")
    else:
        return str("Impossible")


def play(field_data):   # turning out field into matrix (nested list) and printing field
    xn = 0
    on = 0
    global game
    game = [[0 for i in range(3)]for j in range(8)]     # making template of our main matrix
    print("---------")
    for i in range(0, len(field_data), 3):
        print("|", end=' ')
        for n in range(0, 3):
            if field_data[i+n] == "X":
                xn = xn + 1
            elif field_data[i+n] == "O":
                on = on + 1
            if field_data[i+n] == "_":
                print(" ", end=' ')
            else:
                print(field_data[i + n], end=' ')
            game[i//3][n] = field_data[i+n]
            game[n+3][i//3] = field_data[i+n]
        game[6][i//3] = game[i//3][i//3]
        game[7][i//3] = game[i//3][2-i//3]
        print("|")
    print("---------")
    if xn - on < 2 and on - xn < 2:
        return wincheck(game)
    else:
        return str("Impossible")


a = "_________"
mark = "X"
while play(a) == "Game not finished":
    b = [[a[x + (3 * j)] for x in range(0, 3)] for j in range(2, -1, -1)]   # inverted field for
    xy = input("Enter coordinates: > ").split()                             # cords [x][y]
    if ''.join(xy).isdigit():
        if ('1' <= xy[0] <= '3') and ('1' <= xy[1] <= '3'):
            if b[int(xy[1]) - 1][int(xy[0]) - 1] == "_":
                b[int(xy[1]) - 1][int(xy[0]) - 1] = mark
                if b[int(xy[1]) - 1][int(xy[0]) - 1] != "X":
                    mark = "X"
                else:
                    mark = "O"
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
    a = ''.join([b[i][j] for i in range(2, -1, -1) for j in range(0, 3)])
else:
    print(wincheck(game))
