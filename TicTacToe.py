import random

game = [' '] * 9
winner_list = []
played_games = []


def move():
    move = 10 - game.count(' ')
    player = "X" if move % 2 == 1 else "O"

    pos = random.randint(0, 8)
    while game[pos] is not ' ':
        pos = random.randint(0, 8)

    game[pos] = player

def print_game():
    output =  "\n    A   B   C\n"
    output += "  +---+---+---+\n"

    for row in range(3):
        output += "{} |".format(row+1)

        for col in range(3):
            output += " {} |".format(game[(3*row) + col])
        output += "\n  +---+---+---+\n"

    print(output)

def check_winner():
    for row in range(0, 7, 3):
        if game[row:row + 3].count("X") == 3 or game[row:row + 3].count("O") == 3:
            return game[row]

    for col in range(3):
        if game[col:col + 7:3].count("X") == 3 or game[col:col + 7:3].count("O") == 3:
            return game[col]

    if game[0:9:4].count("X") == 3 or game[0:9:4].count("O") == 3:
        return game[0]
    elif game[2:7:2].count("X") == 3 or game[2:7:2].count("O") == 3:
        return game[2]
    else:
        return " "


def print_statistic():
    print("\r " + str(winner_list.count("X")) + "  " + str(winner_list.count("O")) + "  " + str(winner_list.count("T")),
          end=' ')

while True:
    #if len(winner_list) == 957:
        #print("jetzt")

    move()
    winner = check_winner()

    if winner != " ":
        if game not in played_games:
            played_games.append(game)
            winner_list.append(winner)
            print_statistic()
            #print_game()
        game = [' '] * 9
        winner = " "

    elif game.count(' ') == 0:
        if game not in played_games:
            played_games.append(game)
            winner_list.append("T")
            print_statistic()
            #print_game()
        game = [' '] * 9
        winner = " "
