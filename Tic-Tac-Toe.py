note = "This is the wonderful game of Tic-Tac-Toe a fun two player game!\n"
board = [['-','-','-'],
['-','-','-'],
['-','-','-']]

active_game = True
count = 0 

def print_board():
    for space in board:
        print(space)
        print('               \n\n')

def player1_choice():
    user1_input = input("Player 1 choose from 1-9!: \n")
    limit = 0
    if limit < 100:

        if user1_input == '1':
            board[0][0] = 'x' 
        elif user1_input == '2':
            board[0][1] = 'x'
        elif user1_input == '3':
            board[0][2] = 'x'
        elif user1_input == '4':
            board[1][0] = 'x'
        elif user1_input == '5':
            board[1][1] = 'x'
        elif user1_input == '6':
            board[1][2] = 'x'
        elif user1_input == '7':
            board[2][0] = 'x'
        elif user1_input == '8':
            board[2][1] = 'x'
        elif user1_input == '9':
            board[2][2] = 'x'
        else:
            player1_choice()
    else:
        print("Too many wrong choices!!")
    
    print_board()
    if active_game == False:
        print("Good Game player 1 wins")
def player2_choice():
    user2_input = input("Player 2 choose a space from 1-9!: \n")
    limit = 0
    if limit < 100:
        if user2_input == '1' and board[0][0] == '-':
            board[0][0] = '0' 
        elif user2_input == '2':
            board[0][1] = '0'
        elif user2_input == '3':
            board[0][2] = '0'
        elif user2_input == '4':
            board[1][0] = '0'
        elif user2_input == '5':
            board[1][1] = '0'
        elif user2_input == '6':
            board[1][2] = '0'
        elif user2_input == '7':
            board[2][0] = '0'
        elif user2_input == '8':
            board[2][1] = '0'
        elif user2_input == '9':
            board[2][2] = '0'
        else:
            player2_choice()
            limit += 1
    else:
        print("Too many wrong choice")


def tie_check():
    global active_game
    if count > 9:
        active_game = False
        print("This game has ended in a tie")
def check():
    global active_game 
    row1 = board[0][0] == board[0][1] == board[0][2] != '-'
    row2 = board[1][0] == board[1][1] == board[1][2] != '-'
    row3 = board[2][0] == board[2][1] == board[2][2] != '-'

    column1 = board[0][0] == board[1][0] == board[2][0] != '-'
    column2 = board[0][1] == board[1][1] == board[2][1] != '-'
    column3 = board[0][2] == board[1][2] == board[2][2] != '-'

    diagonal1 = board[0][0] == board[1][1] == board[2][2] != '-'
    diagonal2 = board[2][0] == board[1][1] == board[0][2] != '-'



    if row1 == True:
        active_game = False
        return board[0][0]
    elif row2 == True:
        active_game = False
        return board[1][0]
    elif row3 == True:
        active_game = False
        return board[2][0]
    elif column1 == True:
        active_game = False
        return board[1][0]
    elif column2 == True:
        active_game = False
        return board[1][1]
    elif column3 == True:
        active_game = False
        return board[1][2]
    elif diagonal2 == True:
        active_game = False
        return board[1][1]
    elif diagonal1 == True:
        active_game = False
        return board[1][1]


def start_game():
    print(note)
    print_board()
    global active_game 
    global count
    while active_game == True:
        player1_choice()
        count += 1
        tie_check()
        check()
        if active_game == False:
            print("Player 1 wins the game!\n Hope you play again soon :)\n")
            break
        
        player2_choice()
        count += 1
        tie_check()
        check()
        print_board()
        if active_game == False:
            print("Player 2 wins the game!\n Hope you play again soon :)\n")
            break

start_game()
