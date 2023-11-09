from utils import scores, equals3, INITIAL_TABLE, NUMBER_TABLE, Player

turn = Player.COMPUTER
table = INITIAL_TABLE
winner = 0


def win_announcement():
    global table
    global winner
    print("----------------------------------")
    for i in range(0, 3):
        print(table[i])
    print()
    
    for i in range(0, 3):
        print(NUMBER_TABLE[i])
    print()

    if winner == Player.USER:
        print("Congratulations! You won :)")
        return

    if winner == Player.COMPUTER:
        print("Oopsie. The computer won :(")
        return
    
    print("Nobody won. It's a draw")

def find_number_in_table(number):
    for i in range(0, 3):
        for j in range(0, 3):
            if NUMBER_TABLE[i][j] == number:
                return i, j
    
    return -1, -1

def is_completed():
    global table
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if table[i][j] == 0:
                count += 1
    
    return count == 0

def check_winner():
    global table
    global winner

    for i in range(0, 3):
        if equals3(table[i][0], table[i][1], table[i][2]):
            winner = table[i][0]

    for i in range(0, 3):
        if equals3(table[0][i], table[1][i], table[2][i]):
            winner = table[0][i]

    if equals3(table[0][0], table[1][1], table[2][2]):
        winner = table[0][0]
    
    if equals3(table[0][2], table[1][1], table[2][0]):
        winner = table[0][2]

def best_move():
    global table
    global turn
    best_score = -float('inf');
    c_i, c_j = -1, -1

    for i in range(0, 3):
        for j in range(0, 3):
            if table[i][j] == 0:
                table[i][j] = Player.COMPUTER
                score = minimax(3, False)
                table[i][j] = 0

                if score > best_score:
                    best_score = score
                    c_i, c_j = i, j
    
    return NUMBER_TABLE[c_i][c_j]

def minimax(depth, is_maximizing):
    global table
    global winner
    
    check_winner()
    if winner or depth == 0:
        score = scores[winner]
        winner = 0
        return score
    
    if is_maximizing:
        best_score = -float('inf')

        for i in range(0, 3):
            for j in range(0, 3):
                if table[i][j] == 0:
                    table[i][j] = Player.COMPUTER
                    score = minimax(depth - 1, False)
                    table[i][j] = 0

                    best_score = max(score, best_score)
        
        return best_score
    else:
        best_score = float('inf')

        for i in range(0, 3):
            for j in range(0, 3):
                if table[i][j] == 0:
                    table[i][j] = Player.USER
                    score = minimax(depth - 1, True)
                    table[i][j] = 0

                    best_score = min(score, best_score)
        
        return best_score

def main():
    global turn
    global table
    global winner
    print("Hello. You are going to play the game 'Number Scrabble'.\n")
    
    print(is_completed(), winner)
    while not is_completed() and winner == 0:
        print(f"Turn: {turn}")
        for i in range(0, 3):
            print(table[i])
        print()
        
        for i in range(0, 3):
            print(NUMBER_TABLE[i])
        print()

        if turn == Player.USER:
            user_input = input("Enter your next number: ")
            user_number = int(user_input)

            i, j = find_number_in_table(user_number)

            print(table, i, j)

            if table[i][j] == 0:
                table[i][j] = Player.USER
                turn = Player.COMPUTER
            else:
                print(f"[USER] The number {user_number} is already chosen")
        elif turn == Player.COMPUTER:
            comp_number = best_move()
            i, j = find_number_in_table(comp_number)

            if table[i][j] == 0:
                table[i][j] = Player.COMPUTER
                turn = Player.USER
            else:
                print(f"[COMPUTER] The number {comp_number} is already chosen")

        check_winner()
        print(f"[WINNER][{winner}]")

    win_announcement()

if __name__ == "__main__":
    main()
