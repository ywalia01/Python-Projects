#from IPython.display import clear_output

def display_board(board):
    #clear_output()

    print("  ","|"," ","|","")
    print("",board[7],"|",board[8],"|",board[9],"")
    print("  ","|"," ","|","")
    print("-----------")
    print("  ","|"," ","|","")
    print("",board[4],"|",board[5],"|",board[6],"")
    print("  ","|"," ","|","")
    print("-----------")
    print("  ","|"," ","|","")
    print("",board[1],"|",board[2],"|",board[3],"")
    print("  ","|"," ","|","")

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker=input("Player 1, choose X or O:").upper()
    player1 = marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return player1,player2

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[7]==board[8]==board[9]==mark) or
            (board[1]==board[4]==board[7]==mark) or
            (board[2]==board[5]==board[8]==mark) or
            (board[3]==board[6]==board[9]==mark) or
            (board[1]==board[5]==board[9]==mark) or
            (board[3]==board[5]==board[7]==mark))

import random

def choose_first():
    flip=random.randint(0,1)
    if flip:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position: (1-9)"))

    return position

def replay():
    choice=input("Play again? Enter Yes or No")
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? y or n?')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 Wins!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 Wins!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

