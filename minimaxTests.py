# Author:    James McCafferty
# Created:   26.03.2024

import unittest
from board import Board
from minimax import minimax
import numpy as np

class TestMinimax(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_minimax_win_for_ai(self):
        # Minimax is about to win, minimax should place the fith piece in the chain
        self.board.board[0][0] = 2
        self.board.board[0][1] = 2
        self.board.board[0][2] = 2
        self.board.board[0][3] = 2

        self.board.board[1][1] = 1
        self.board.board[2][2] = 1
        self.board.board[3][3] = 1

        evaluation, ai_move = minimax(self.board, self.board.board, 2, True)
        self.assertTrue(np.array_equal(ai_move, np.array([0, 4])))

    def test_ai_blocks_human_win(self):
        # Human is about to win, minimax should block it

        self.board.board.fill(0)  

        self.board.board[0][0] = 1
        self.board.board[0][1] = 1
        self.board.board[0][2] = 1
        self.board.board[0][3] = 1

        self.board.board[1][1] = 2
        self.board.board[2][2] = 2
        self.board.board[3][3] = 2

        evaluation, ai_move = minimax(self.board, self.board.board, 2, True)
        self.assertTrue(np.array_equal(ai_move, np.array([0, 4])))

if __name__ == '__main__':
    unittest.main(verbosity=2)
