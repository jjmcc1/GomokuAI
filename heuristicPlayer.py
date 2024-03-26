import copy
from constants import ROWS, COLUMNS
import numpy as np

def heuristic_player(board):
        copied_board = copy.deepcopy(board)
        # Going through horizontally and scoring with reference to player 1's moves
        for r in range(ROWS):
            inARow = 0
            for c in range(COLUMNS):
                if copied_board[r][c] == 1:
                    inARow += 1
                else:
                    inARow = 0
                if inARow >= 1 and inARow <= 4:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= (inARow*10):
                        copied_board[r][c - inARow] = (inARow * 10)
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= (inARow*10):
                        copied_board[r][c + 1] = (inARow * 10)
                    print(copied_board)
                                
        # Going through vertically and scoring with reference to player 1's moves
        for c in range(COLUMNS):
            inARow = 0
            for r in range(ROWS):
                if copied_board[r][c] == 1:
                    inARow += 1
                else:
                    inARow = 0
                if inARow >= 1 and inARow <= 4:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= (inARow*10):
                        copied_board[r-inARow][c] = (inARow * 10)
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= (inARow*10):
                        copied_board[r+1][c] = (inARow * 10)
                    # print(copied_board)
        
        # Scoring diagonals in relation to player 1's moves
        for i in range(0,4):
            copied_board = np.rot90(copied_board, i)
            r = ROWS
            c = 0
            for r in range(r, -1, -1):
                inARow = 0
                for r, c in zip(range(r, ROWS, 1), range(COLUMNS)):
                    if copied_board[r][c] == 1:
                        inARow += 1
                    else: 
                        inARow = 0
                    if inARow >= 1 and inARow <= 4:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= (inARow*10):
                            copied_board[r-inARow][c-inARow] = (inARow * 10)
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= (inARow*10):
                            copied_board[r+1][c+1] = (inARow * 10)  

        copied_board = np.rot90(copied_board, -2)         
        print(copied_board)    
                                
        # Going through horizontally and scoring with reference to player 2's moves
        for r in range(ROWS):
                    inARow = 0
                    for c in range(COLUMNS):
                        if copied_board[r][c] == 2:
                            inARow += 1
                        else:
                            inARow = 0
                        if inARow >= 1 and inARow <= 4:
                            if inARow == 1:
                                if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= ((inARow*10)+11):
                                    copied_board[r][c - inARow] = ((inARow * 10)+11)
                                if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= ((inARow*10)+11):
                                    copied_board[r][c + 1] = ((inARow * 10)+11)
                            if inARow == 2:
                                if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= ((inARow*10)+2):
                                    copied_board[r][c - inARow] = ((inARow*10)+2)
                                if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= ((inARow*10)+2):
                                    copied_board[r][c + 1] = ((inARow*10)+2)
                            if inARow == 3:
                                if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= ((inARow*10)-1):
                                    copied_board[r][c - inARow] = ((inARow * 10)-1)
                                if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= ((inARow*10)-1):
                                    copied_board[r][c + 1] = ((inARow * 10)-1)
                            if inARow == 4:
                                if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= (inARow*10):
                                    copied_board[r][c - inARow] = ((inARow * 10)+10)
                                if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= (inARow*10):
                                    copied_board[r][c + 1] = ((inARow * 10)+10)

        # Going through vertically and scoring with reference to player 2's moves
        for c in range(COLUMNS):
                    inARow = 0
                    for r in range(ROWS):
                        if copied_board[r][c] == 2:
                            inARow += 1
                        else:
                            inARow = 0
                        if inARow >= 1 and inARow <= 4:
                            if inARow == 1:
                                if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= ((inARow*10)+11):
                                    copied_board[r-inARow][c] = ((inARow*10)+11)
                                if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= ((inARow*10)+11):
                                    copied_board[r+1][c] = ((inARow*10)+11)
                            if inARow == 2:
                                if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= ((inARow*10)+2):
                                    copied_board[r-inARow][c] = ((inARow*10)+2)
                                if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= ((inARow*10)+2):
                                    copied_board[r+1][c] = ((inARow*10)+2)
                            if inARow == 3:
                                if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= ((inARow * 10)-1):
                                    copied_board[r-inARow][c] = ((inARow * 10)-1)
                                if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= ((inARow * 10)-1):
                                    copied_board[r+1][c] = ((inARow * 10)-1)
                            if inARow == 4:
                                if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= ((inARow * 10)+10):
                                    copied_board[r-inARow][c] = ((inARow * 10)+10)
                                if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= ((inARow * 10)+10):
                                    copied_board[r+1][c] = ((inARow * 10)+10)

        # Scoring diagonals in relation to player 2's moves
        for i in range(0,4):
            copied_board = np.rot90(copied_board, i)
            r = ROWS
            c = 0
            for r in range(r, -1, -1):
                inARow = 0
                for r, c in zip(range(r, ROWS, 1), range(COLUMNS)):
                    if copied_board[r][c] == 2:
                        inARow += 1
                    else: 
                        inARow = 0
                    if inARow >= 1 and inARow <= 4:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= (inARow*10):
                            copied_board[r-inARow][c-inARow] = (inARow * 10) + 1
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= (inARow*10):
                            copied_board[r+1][c+1] = (inARow * 10) + 1 

        copied_board = np.rot90(copied_board, -2)         
        print(copied_board) 

        highest_score = np.unravel_index(np.argmax(copied_board, axis=None), (ROWS, COLUMNS))           # numpy's argmax when used with the axis as None it flattens the array and finds the highest value
        # print(highest_score)                                                                          # (ROWS, COLUMNS) is the shape of the board
        return highest_score # This actually returns the coordinates of the highest score on the board  # 'unravel_index' takes the index of the highest score returned by argmax for the flattend array
                                                                                                        # - and changes it into coordinates (row, column) that can be used for a move