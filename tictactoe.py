import random


def display_board(board):
    print("\n" *50)

    print('   |   |')
    print(' ' +board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    #across
    return((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    #down
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    #diagonal
    (board[7] == board[5] == board[3] == mark) or
    (board[1] == board[5] == board[9] == mark))


def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if we return True
    return True


def player_choice(board):

    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your position: (1,9) '))

    return position


def replay():

    return input("Play again? Enter Yes or No").lower().startswith('y')


print("Welcome to Tic Tac Toe!")

while True:

    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Yes or No?')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            #show the board
            display_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place the marker on the position
            place_marker(the_board, player1_marker, position)

            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    print ("Player 2 turn")
                    turn = "Player 2"

            #or check iff there is a tie

        else:
            # Player 2 turn

            display_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place the marker on the position
            place_marker(the_board, player2_marker, position)

            #check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    print("Player 1 turn")
                    turn = "Player 1"


    if not replay():
        break
