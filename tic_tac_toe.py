"""Tic Tac Toe"""
import os
from random import randint

def display_board(board):
    """Prints a 3x3 board."""
    # os.system('clear')
    print("----------------")
    print(f"| {board[0]}  | {board[1]}  | {board[2]}  |")
    print("----------------")
    print(f"| {board[3]}  | {board[4]}  | {board[5]}  |")
    print("----------------")
    print(f"| {board[6]}  | {board[7]}  | {board[8]}  |")
    print("----------------")

def player_input():
    """Takes player's input and returns his marker(X or O)."""
    player = input("Which player would you like to be? X or O?\n")
    while player not in ('X', 'O'):
        print("Wrong choice! You must choose between player X or O.\n")
        player = input("Which player would you like to be? X or O?\n")
    print(f"You are player {player}.\n")
    return player

def place_marker(board, marker, position):
    """Assigns players's marker to the position he chose."""
    board[position-1] = marker

def win_check(board, mark):
    """Returns True if the player's mark has won; otherwise it returns False."""
    return (board[0]==board[1]==board[2]==mark or
            board[0]==board[3]==board[6]==mark or
            board[0]==board[4]==board[8]==mark or
            board[1]==board[4]==board[7]==mark or
            board[2]==board[5]==board[8]==mark or
            board[2]==board[4]==board[6]==mark)

def choose_first():
    """Returns a string of the marker of the player that will go first."""
    rand_int = randint(1,2)
    if rand_int == 1:
        return 'X'
    return 'O'

def space_check(board, position):
    """Returns True if a position on the board is empty, otherwise it returns False."""
    return board[position-1] == ' '

def full_board_check(board):
    """Returns True if there are no free positions on the board; otherwise it returns False."""
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Returns player's next position, after checking if it is acceptable and free."""
    acceptable = [1,2,3,4,5,6,7,8,9]
    pos = int(input("Please choose a position between 1 and 9.\n"))

    while pos not in acceptable or not space_check(board, pos):
        if pos not in acceptable:
            print("The position you chose is not in the acceptable range (1-9).")
        if not space_check(board, pos):
            print("The position you chose is already filled. Please choose another one.")
        pos = int(input("Please choose a position between 1 and 9.\n"))
    return pos

def replay():
    """Returns True if the player wants to play another round; otherwise it returns False."""
    print("Would you like to play again? Y/N?\n")
    reply = input()
    while reply.upper()!='Y' and reply.upper()!='N':
        reply = input("Please enter Y/N\n")
    return reply.upper()=='Y'

if __name__== "__main__":
    print('Welcome to Tic Tac Toe!\n')
    while True:
        game_on = True
        board = [' ']*10
        player = player_input()

        first_player = choose_first()
        if first_player == 'X':
            second_player = 'O'
        else:
            second_player = 'X'
        print(f"Player {first_player}, you go first.\n")

        while game_on:
            # First player's turn
            position = player_choice(board)
            place_marker(board,first_player,position)
            display_board(board)

            if win_check(board, first_player):
                print(f"Player {first_player}, you won!")
                game_on = False
                break

            if full_board_check(board):
                print("The game is over. No one won.")
                break

            # Second player's turn.
            position = player_choice(board)
            place_marker(board,second_player,position)
            display_board(board)

            if win_check(board, second_player):
                print(f"Player {second_player}, you won!")
                game_on = False

            if full_board_check(board):
                print("The game is over. No one won.")
                game_on = False

        if not replay():
            break
