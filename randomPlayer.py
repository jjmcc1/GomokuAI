import random
from constants import ROWS, COLUMNS

# Returns a random move using the random library function 'randint'
def get_random_move():
    row = random.randint(0, ROWS-1)
    column = random.randint(0, COLUMNS-1)
    move = row, column
    return move