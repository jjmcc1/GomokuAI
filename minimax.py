# Author:    James McCafferty
# Created:   26.03.2024

import pygame
import numpy as np
import copy
from constants import PLAYER_1, PLAYER_2, ROWS, COLUMNS

def minimax(boardO, board, max_depth, max_player, alpha = float("-inf"), beta = float("inf")):
    # Base Case
    # If win for Maximising player (AI 2), return 10000 + max_depth (higher reward for closer wins)
    if boardO.checkWinner(board, 2):
        # print("Win for ai, returning " + str(10000+max_depth))
        return 10000 + max_depth, None
    # If win for Minimising player (Human 1), return -10000 - max_depth (lower score for closer loss)
    if boardO.checkWinner(board, 1):
        # print("Win for human, returning " + str(-10000-max_depth))
        return -10000 - max_depth, None
    # If game ends in a draw, return 0
    if boardO.check_if_draw(board, False):
        # print("Draw, returning 0")
        return 0, None
    # If max_depth is reached, return evaluation of board from board_scorer
    if max_depth == 0:
        evaluation = boardO.board_scorer(board)
        # print("Max depth reached, returning " + str(evaluation))
        return evaluation, None

    # If maximising
    if max_player:
        best_move = None
        for move in get_moves(boardO, board):                                               # Goes through all moves returned by get_moves
            temp_board = copy.deepcopy(board)                                               # Creates a copy of the current board
            updated_board = simulate_move(boardO, temp_board, move, PLAYER_2)               # Updated board is the temporary board after the move has been made 
            evaluation = minimax(boardO, updated_board, max_depth-1, False, alpha, beta)[0] # Pass the new board into minimax
            evaluation -= max_depth                                                         # Set the evaluation equal to itself minus the max_depth
            alpha = max(alpha, evaluation)                                                  # Alpha is highest between current alpha and the result from MIN
            if alpha == evaluation:                                                         # When alpha is equal to the evaluation set that as the best move
                best_move = move
            if alpha >= beta:                                                               # Prune when MIN(beta) has better alternative
                break
        return alpha, best_move                                                             # Return alpha(evaluation) and the best move
    else: # If minimising
        best_move = None
        for move in get_moves(boardO, board):
            temp_board = copy.deepcopy(board)
            updated_board = simulate_move(boardO, temp_board, move, PLAYER_1)
            evaluation = minimax(boardO, updated_board, max_depth-1, True, alpha, beta)[0]  # [0] is used to only get the evaluation returned by MAX rather 
            evaluation += max_depth                                                         # - than getting the move too.
            beta = min(beta, evaluation)                                                    # Beta is lowest between current beta and the result from MAX
            if beta == evaluation:
                best_move = move
            if beta <= alpha:                                                               # Prune when MAX(alpha) has better alternative
                break
        return beta, best_move                                                              # Return beta(evaluation) and the best move

# Places a piece on the copied board (temp_board)
def simulate_move(boardO, board, move, player):
    temp_board = copy.deepcopy(board)                                            # Creates a copy of the board using deepcopy from the copy library
    boardO.placePiece(temp_board, move, player)                                  # Places a piece on the copied board to simulate a real move    
    # print("simulate_move: Placing piece on temp_board at: " + str(move))
    return temp_board

# Returns a list of coords of the possible moves
def get_moves(boardO, board):
    move_array = boardO.potential_moves(board)              # potential_moves applies scores to every move around existing pieces        
    move_coords = np.transpose(np.where(move_array >= 10))  # For every position on the board that potential_moves returns, if it is over 10 
    return move_coords                                      # - add it's indexes to a tuple of arrays, in the tuples use transpose to convert the indexes
                                                            # - into a list of move coordinates (move_coords) e.g. the moves that minimax can make
