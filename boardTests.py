# Author:    James McCafferty
# Created:   26.03.2024
import unittest
from constants import PLAYER_1, PLAYER_2
from board import Board
# This class tests the board functions
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    # Tests the __init__ constructor
    def test_constructor(self):
        self.assertEqual(self.board.board.shape, (15, 15))
    
    # Testing is_pos_full function
    def test_pos_full(self):
        move = (9, 9)
        self.assertFalse(self.board.is_pos_full(move))
        self.board.place_piece(move, PLAYER_1)
        self.assertTrue(self.board.is_pos_full(move))
    
    # Testing place_piece function
    def test_place_p(self):
        # Tests player 1's move
        move = (5, 8)
        self.board.place_piece(move, PLAYER_1)
        self.assertEqual(self.board.board[5][8], PLAYER_1)
        # Tests player 2's move
        move = (1, 3)
        self.board.place_piece(move, PLAYER_2)
        self.assertEqual(self.board.board[1][3], PLAYER_2)
   
    # Testing check_if_winner() and checkWinner()
    def test_winner(self):  
        self.assertFalse(self.board.check_if_winner(PLAYER_1)) # Tests when game is not won for player 1
        self.assertFalse(self.board.check_if_winner(PLAYER_2)) # Tests when game is not won for player 2
        # Testing when (Player 1) has 5 pieces in a row
        self.board.board[0][0] = 1
        self.board.board[0][1] = 1
        self.board.board[0][2] = 1
        self.board.board[0][3] = 1
        self.board.board[0][4] = 1
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_1))
        # Testing when (Player 1) has 5 pieces in a column
        self.board.board.fill(0)                # Resets the board to be empty
        self.board.board[0][0] = 1
        self.board.board[1][0] = 1
        self.board.board[2][0] = 1
        self.board.board[3][0] = 1
        self.board.board[4][0] = 1
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_1))
        # Testing when (Player 1) has 5 pieces in a diagonal
        self.board.board.fill(0)                # Resets the board to be empty
        self.board.board[0][0] = 1
        self.board.board[1][1] = 1
        self.board.board[2][2] = 1
        self.board.board[3][3] = 1
        self.board.board[4][4] = 1
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_1))

        # Testing when (Player 2) has 5 pieces in a row,
        self.board.board.fill(0)                # Resets the board to be empty
        self.board.board[0][0] = 2
        self.board.board[0][1] = 2
        self.board.board[0][2] = 2
        self.board.board[0][3] = 2
        self.board.board[0][4] = 2
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_2))
        # Testing when (Player 2) has 5 pieces in a column
        self.board.board.fill(0)                # Resets the board to be empty
        self.board.board[0][0] = 2
        self.board.board[1][0] = 2
        self.board.board[2][0] = 2
        self.board.board[3][0] = 2
        self.board.board[4][0] = 2
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_2))
        # Testing when (Player 2) has 5 pieces in a diagonal
        self.board.board.fill(0)                # Resets the board to be empty
        self.board.board[0][0] = 2
        self.board.board[1][1] = 2
        self.board.board[2][2] = 2
        self.board.board[3][3] = 2
        self.board.board[4][4] = 2
        self.assertTrue(self.board.checkWinner(self.board.board, PLAYER_2))
     
    # Testing check_if_draw()
    def test_draw(self):
        # Test when the game is not a draw
        self.assertFalse(self.board.check_if_draw(self.board.board, False))
        # Test when the game is a draw
        self.board.board.fill(1)            # Fills entire array with ones
        self.board.board[7:,0:] = 2         # [7:, 0:] From the seventh row and 0th column onwards it's just two's
        self.assertTrue(self.board.check_if_draw(self.board.board, False))  # Passing in isWon as false to check when the board is full of 1's and 2's 
    
if __name__ == '__main__':
    unittest.main(verbosity=2) # Verbosity = 2 is used to provide more details on the tests that are run and the results of each
