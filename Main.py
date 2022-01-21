import os
from Utilities import game_start_ran, clear, playagain
from checking_functions import space_checkboard, win_check, fullboard_check, player_choice
from Utilities import display_game, player_select, place_marker 
#Welcome to Tic Tac Toe Game!

print("Welcome Tic Tac Toe !\n")

def ready():
    start="f"
    while start.lower() not in ["no","yes"]:
        start=input("Are you ready guys Yes or No ? ")
        if start.lower() not in ["no","yes"]:
            print("Please say Yes or No! ")
    if start.lower()=="yes":
        return True
    else:
        return False

game_on=ready()

while game_on==True:
    theBoard = [" "] * 10
    player=game_start_ran()
    print(player + ' will go first.')
    mark_player1,mark_player2=player_select()
    while game_on==True:
        if player=="Player 1":
            #PLayer1's turn
            display_game(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,position,mark_player1)
            if win_check(theBoard,mark_player1):
                display_game(theBoard)
                print("Congratulations, You have won the game!!!")
                game_on=False
            else:
                if fullboard_check(theBoard):
                    display_game(theBoard)
                    print("The game is draw !!!")
                    game_on=False
                else:
                    player="Player 2"
        else:   
            #Player2's turn
            display_game(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,position,mark_player2)
            if win_check(theBoard,mark_player2):
                display_game(theBoard)
                print("Congratulations, You have won the game!!!")
                game_on=False
            else:
                if fullboard_check(theBoard):
                    display_game(theBoard)
                    print("The game is draw !!!")
                    game_on=False
                else:
                    player="Player 1"
            
            
            
    game_on=playagain()
    if game_on==False:
        print("Thanks for playing Tic Tac Toe game")
        break
else:
    print("Thanks")