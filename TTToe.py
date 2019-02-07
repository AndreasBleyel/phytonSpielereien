#game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#game = [' ' for i in range(9)]
game = [' '] * 9
inputs = {"A1":0, "A2":3, "A3":6, "B1":1, "B2":4, "B3":7, "C1":2, "C2":5, "C3":8}

def print_game():
    output =  "    A   B   C\n"
    output += "  +---+---+---+\n"

    for row in range(3):
        output += "{} |".format(row+1)

        for col in range(3):
            output += " {} |".format(game[(3*row) + col])
        output += "\n  +---+---+---+\n"

    print(output)

def move():
    move = 10 - game.count(' ')
    player = "X" if move % 2 == 1 else "O"
    pos = check_input(input("  {}. Zug {}:".format(move, player)))

    if pos != -1:
        game[pos] = player

def check_input(input):
    if input in inputs and game[inputs[input]] == ' ':
        return inputs[input]
    else:
        return -1

def check_winner():
    for row in range(0, 7, 3):
        if game[row:row+3].count("X") == 3 or game[row:row+3].count("O") == 3:
            return game[row]

    for col in range(3):
        if game[col:col+7:3].count("X") == 3 or game[col:col+7:3].count("O") == 3:
            return game[col]

    if game[0:9:4].count("X") == 3 or game[0:9:4].count("O") == 3:
        return game[0]
    elif game[2:7:2].count("X") == 3 or game[2:7:2].count("O") == 3:
        return game[2]
    else:
        return " "


while True:
    print_game()
    move()
    winner = check_winner()

    if winner != " ":
        print_game()
        print("Gewinner: " + winner)
        break
    elif game.count(' ') == 0:
        print_game()
        print("Unentschieden: Keiner hat gewonnen")
        break