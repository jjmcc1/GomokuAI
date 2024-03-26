import unittest
from board import Board
from constants import PLAYER_1, PLAYER_2
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    # Tests the __init__ constructor
    def test_constructor(self):
        self.assertIsInstance(self.game.board, Board)
        self.assertEqual(self.game.player, PLAYER_1)
    
    # Tests the switch_player function
    def test_switch(self):
        self.game.switch_player()
        self.assertEqual(self.game.player, PLAYER_2)
        self.game.switch_player()
        self.assertEqual(self.game.player, PLAYER_1)

if __name__ == '__main__':
    unittest.main(verbosity=2)