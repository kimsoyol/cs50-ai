"""
Tic Tac Toe Player
"""
import copy
import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_moves = 0
    o_moves = 0

    for row in board:
        x_moves += row.count(X)
        o_moves += row.count(O)

    if x_moves == 0 and o_moves == 0:
        return X
    elif x_moves > o_moves:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions =  {(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value is None}
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board = copy.deepcopy(board)
    possible_actions = actions(board)
    if not action in possible_actions:
        print(action)
        raise ValueError("Invalid action")

    current_player = player(board)
    copy_board[action[0]][action[1]] = current_player
    # print(copy_board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None  # No winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif not winner(board) and not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    current_winner = winner(board)

    if current_winner is X:
        return 1
    elif current_winner is O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player is X:
        v, best_move = max_value(board)
    else:
        v, best_move = min_value(board)

    print(best_move)
    return best_move

def max_value(state):
    if terminal(state):
        return utility(state), None

    v = -math.inf
    move = None
    for action in actions(state):
        score, z = min_value(result(state, action))
        if score > v:
            v = score
            move = action
            if v == 1:
                return v, move
    print('max-value:', v)
    return v, move

def min_value(state):
    if terminal(state):
        return utility(state), None

    v = math.inf
    move = None
    for action in actions(state):
        score, z = max_value(result(state, action))
        if score < v:
            v = score
            move = action
            if v == -1:
                return v, move

    print('min-value:', v)
    return v, move
