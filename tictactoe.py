import random

def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])

#display_board(test_board)

def player_marker():
    choice = ' '
    while choice not in ['X', 'O']:
        choice = input("Player 1, choose X or O ").upper()
    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return(player1, player2)



def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[1] == marker and board[5] == marker and board[9] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[5] == marker and board[7] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker))


def choose_first():
        turn = random.randint(1,2)
        return "Player {} you go first".format(turn)


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Enter a number for the board position of your choice (1-9) "))
        if position not in range(1, 10):
            print("Try Again")    
    return position

def replay():
    ans = ' '
    while ans not in ['Y', 'N']:
        ans = input("Do you want to play again? (Y/N) ").upper()
        if ans.isdigit() or ans not in ['Y','N']:
            print("That's not a correct answer, try again")
    return True if ans == 'Y' else False

print("Welcome to Tic Tac Toe!")
while True:
    board = [' '] * 10
    game_on = True
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn)
    while game_on:
        if turn == "Player 1 you go first":
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board,player1_marker):
                display_board(board)
                print("Congrats! Player 1 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    turn = "Player 2 you go first"
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print("Congrats! Player 2 won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    turn = "Player 1 you go first"
    if not replay():
        break


