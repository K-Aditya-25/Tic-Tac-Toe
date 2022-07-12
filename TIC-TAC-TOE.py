def display_board(board):
    print('\n'*100)
    print("Here is the board!")
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input():
    player1_marker=''
    player2_marker=''
    while player1_marker.upper()!='X' and player1_marker.upper()!='O':
        player1_marker=input("Player 1: X or O? (X/O)")
        if player1_marker.upper()=='X':
            player2_marker='O'
        elif player1_marker.upper()=='O':
            player2_marker='X'
        else:
            print("Invalid Choice!")
    return (player1_marker.upper(),player2_marker.upper())

from random import randint
def turn():
    a=randint(1,2)
    if a==1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    if board[position]==' ':
        return True
    else:
        return False

def place_marker(board,position,marker):
    board[position]=marker
def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    else:
        return True

def win_check(board,marker):
    return (board[1]==marker and board[2]==marker and board[3]==marker) or (board[4]==marker and board[5]==marker and board[6]==marker) or (board[7]==marker and board[8]==marker and board[9]==marker)or (board[1]==marker and board[4]==marker and board[7]==marker)or (board[2]==marker and board[5]==marker and board[8]==marker)or (board[3]==marker and board[6]==marker and board[9]==marker)or (board[1]==marker and board[5]==marker and board[9]==marker)or (board[3]==marker and board[5]==marker and board[7]==marker)

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Enter the position you wanna fill (1-9) '))
        if position not in range(1,10) or not space_check(board,position):
            print("Invalid input! Try again. ")
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    board=[' ']*10
    ##Set up
    print("Welcome to TIC TAC TOE!")
    player1_marker,player2_marker= player_input()
    choose_random=turn()
    print(choose_random+' will go first')
    
    ##decide to start game
    game_on=input('Are you ready to play? (Y/N) ')
    if game_on.lower()=='y':
        game_on=True
    else:
        game_on=False
    #Start game
    while game_on==True:
        if choose_random=='Player 1':
            display_board(board)
            position=player_choice(board)
            place_marker(board,position,player1_marker)
            display_board(board)
            if win_check(board,player1_marker)==True:
                print("Player 1 has WON!!")
                game_on=False
            else:
                if full_board_check(board)==True:
                    print("It's a TIE!!")
                    game_on=False
                else:
                    choose_random='Player 2'
                    
        else:
            display_board(board)
            position=player_choice(board)
            place_marker(board,position,player2_marker)
            display_board(board)
            if win_check(board,player2_marker)==True:
                print("Player 2 has WON!!")
                game_on=False
            else:
                if full_board_check(board)==True:
                    print("It's a TIE!!")
                    game_on=False
                else:
                    choose_random='Player 1'
    
    if not replay():
        break