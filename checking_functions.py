
#checking space
def space_checkboard(board,position):
    return board[position]==" "

#checking win
def win_check(board,mark):
    return (board[1]==mark and board[2]==mark and board[3]==mark)or(board[4]==mark and board[5]==mark and board[6]==mark)or(board[7]==mark and board[8]==mark and board[9]==mark)or(board[1]==mark and board[4]==mark and board[7]==mark)or(board[2]==mark and board[5]==mark and board[8]==mark)or(board[3]==mark and board[6]==mark and board[9]==mark)or(board[1]==mark and board[5]==mark and board[9]==mark)or(board[3]==mark and board[5]==mark and board[7]==mark)

#checking fullboard
def fullboard_check(board):
    for i in range(1,10):
        if space_checkboard(board, i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_checkboard(board,position):
        position=int(input("Choose your next position (1-9) "))
    return position 