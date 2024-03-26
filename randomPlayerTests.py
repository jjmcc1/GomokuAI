from constants import ROWS, COLUMNS

def test_get_random_move(self):
    move = self.game.get_random_move()
    self.assertIsInstance(move, tuple)
    self.assertGreaterEqual(move[0], 0)
    self.assertLess(move[0], ROWS)
    self.assertGreaterEqual(move[1], 0)
    self.assertLess(move[1], COLUMNS)