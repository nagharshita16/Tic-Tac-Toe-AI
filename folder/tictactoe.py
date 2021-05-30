"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


class NotValidAction(Exception):
    pass

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if(x_count == o_count):
        return X
    else:
        return O


def actions(board):
    actions_to = []
    for row in range(3):
        for cell in range(3):
            if(board[row][cell] == EMPTY):
                actions_to.append((row,cell))
    return set(actions_to)


def result(board, action):
    board_to = copy.deepcopy(board)
    if(board_to[action[0]][action[1]] == EMPTY):
        board_to[action[0]][action[1]] = player(board)
        return board_to
    else:
        raise NotValidAction




def winner(board):
    #Returns the winner if any otherwise returns none
    # parsing row wise
    for row in board:
        if(row[0] == row[1] and row[1] == row[2]):
            return row[0]

    # parsing collumn wise
    for cell in range(3):
        if(board[0][cell] == board[1][cell] and board[1][cell] == board[2][cell]):
            return board[0][cell]

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    if(board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return board[2][0]

    return None



def terminal(board):
    # returns if the game is over
    if(winner(board) != None):
        return True
    for row in board:
        if(EMPTY in row):
            return False

    return True


def utility(board):
    value = winner(board)
    if(value == X):
        return 1

    if(value == O):
        return -1

    if(value == None):
        return 0

def minPlayer(board):
    if(terminal(board)):
        return([None,utility(board)])

    min_val = float('inf')
    action_to_do = ()

    for move in actions(board):
        val = maxPlayer(result(board,move))
        if(min_val > val[1]):
            action_to_do = move
            min_val = val[1]
    return ([action_to_do,min_val])

def maxPlayer(board):
    if(terminal(board)):
        return([None,utility(board)])

    max_val = float('-inf')
    action_to_do = ()

    for move in actions(board):
        val = minPlayer(result(board,move))
        if(max_val < val[1]):
            action_to_do = move
            max_val = val[1]
    return ([action_to_do,max_val])





def minimax(board):
    if(terminal(board)):
        return None


    turn = player(board)
    if(turn == X):
        return(maxPlayer(board)[0])

    else:
        return(minPlayer(board)[0])
















#end
