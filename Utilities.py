import random
import os

def clear():
    os.system('clear')

def game_start_ran():
    if random.randint(0,1)==0:
        return "Player 2"
    else:
        return "Player 1"

def playagain():
    start="f"
    while start.lower() not in ["no","yes"]:
        start=input("Do you want to play again Yes or No ? ")
        if start.lower() not in ["no","yes"]:
            print("Please say Yes or No! ")
    if start.lower()=="yes":
        return True
    else:
        return False

def place_marker(board,position,marker):
    board[position]=marker
   
def display_game(position):
    #clear()
    os.system("clear")
    print("    |   |      ")
    print("  "+position[7]+" | "+position[8]+" | "+position[9])
    print(" _ _|_ _|_ _  ")
    print("    |   |      ")
    print("  "+position[4]+" | "+position[5]+" | "+position[6])
    print(" _ _|_ _|_ _  ")
    print("    |   |      ")
    print("  "+position[1]+" | "+position[2]+" | "+position[3])
    print("    |   | ")

def player_select():
    mark="F"
    while mark not in ["X","O"]:
            mark=input("Player : Do you want to be X or O ?")
            if mark not in ["X","O"]:
                print("Please choose X or O ")
    if mark=="X":
        return "X","O"
    else:
        return "O","X"


