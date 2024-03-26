# Author:    James McCafferty
# Created:   26.03.2024
 

import numpy as np
from constants import ROWS, COLUMNS, WIN_NUMBER, LINE_WIDTH, LINE_COLOUR, GRID_SIZE, BROWN, WIDTH, HEIGHT, BLACK, WHITE, PIECE_RADIUS
import pygame
import copy

class Board:
    # Constructor
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), dtype = np.int32) #  Sets up a 2D numpy array of zeros for the size of board
    # Creates pygame window    
    def create_window(self):
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Gomoku")        # Sets a caption on the pygame window called 'Gomoku'
    # Prints the board (2D numpy array) in the terminal    
    def print_board(self):
        print(self.board)
    # Draws a representation of the current board on the pygame window
    def draw_board(self):
        # Clear screen 
            self.WINDOW.fill(BROWN) # Colours the board brown like the real gomoku board

            for i in range(1, ROWS + 1):    # Draw horizontal lines with GRID_SIZE margin front and back
                pygame.draw.line(self.WINDOW, LINE_COLOUR, (GRID_SIZE, i * GRID_SIZE), (GRID_SIZE * COLUMNS, i * GRID_SIZE), LINE_WIDTH)
            
            for i in range(1, COLUMNS + 1):    # Draw vertical lines with GRID_SIZE margin top and bottom
                pygame.draw.line(self.WINDOW, LINE_COLOUR, (i * GRID_SIZE, GRID_SIZE), (i * GRID_SIZE, GRID_SIZE * ROWS), LINE_WIDTH)

            # Draw pieces
            for c in range(COLUMNS):
                x = GRID_SIZE*c + GRID_SIZE
                for r in range(ROWS):
                    y = GRID_SIZE*r + GRID_SIZE
                    if self.board[r][c] == 1:
                        pygame.draw.circle(self.WINDOW, BLACK, (x, y), PIECE_RADIUS)
                    elif self.board[r][c] == 2:
                        pygame.draw.circle(self.WINDOW, WHITE, (x, y), PIECE_RADIUS)
            pygame.display.update()
        
    # Returns boolean, true for full, false for free
    def is_pos_full(self, move):
        row, column = move
        return self.board[row, column] != 0.
           
    # Returns evaluation for current board state
    def board_scorer(self, board):
        copied_board = copy.deepcopy(board)
        # Going through horizontally and scoring with reference to player 1's (Human player) moves
        for r in range(ROWS):
            inARow = 0
            for c in range(COLUMNS):
                if copied_board[r][c] == 1:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= 70:
                        copied_board[r][c - inARow] = 70
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= 70:
                        copied_board[r][c + 1] = 70
                if inARow == 4:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= 255:
                        copied_board[r][c - inARow] = 255
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= 255:
                        copied_board[r][c + 1] = 255
                                
        # Going through vertically and scoring with reference to player 1's moves
        for c in range(COLUMNS):
            inARow = 0
            for r in range(ROWS):
                if copied_board[r][c] == 1:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= 70:
                        copied_board[r-inARow][c] = 70
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= 70:
                        copied_board[r+1][c] = 70
                if inARow == 4:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= 255:
                        copied_board[r-inARow][c] = 255
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= 255:
                        copied_board[r+1][c] = 255
                     
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
                    if inARow == 3:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= 70:
                            copied_board[r-inARow][c-inARow] = 70
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= 70:
                            copied_board[r+1][c+1] = 70
                    if inARow == 4:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= 255:
                            copied_board[r-inARow][c-inARow] = 255
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= 255:
                            copied_board[r+1][c+1] = 255
            
        copied_board = np.rot90(copied_board, -2)   # Reverses the rotation to get back to the orginal orientation      
        # print(copied_board)   
        # Makes use of a boolean mask to make sure 1's and 2's are not included in the sum
        bmask = np.where((copied_board != 1)&(copied_board!= 2)) 
        minSum = np.sum(copied_board[bmask])
        # print("minSum = " + str(minSum))

        copied_board = copy.deepcopy(board)
        # Going through horizontally and scoring with reference to player 2's (AI player) moves                
        for r in range(ROWS):
            inARow = 0
            for c in range(COLUMNS):
                if copied_board[r][c] == 2:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 2:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= 20:
                        copied_board[r][c - inARow] = 20
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= 20:
                        copied_board[r][c + 1] = 20
                if inARow == 3:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= 125:
                        copied_board[r][c - inARow] = 125
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= 125:
                        copied_board[r][c + 1] = 125
                if inARow == 4:
                    if c - inARow >= 0 and (copied_board[r][c - inARow] != 1 and copied_board[r][c - inARow] != 2) and copied_board[r][c-inARow] <= 550:
                        copied_board[r][c - inARow] = 550
                    if c + 1 < COLUMNS and (copied_board[r][c + 1] != 1 and copied_board[r][c + 1] != 2) and copied_board[r][c+1] <= 550:
                        copied_board[r][c + 1] = 550
                                
        # Going through vertically and scoring with reference to player 2's moves
        for c in range(COLUMNS):
            inARow = 0
            for r in range(ROWS):
                if copied_board[r][c] == 2:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 2:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= 20:
                        copied_board[r-inARow][c] = 20
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= 20:
                        copied_board[r+1][c] = 20
                if inARow == 3:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= 125:
                        copied_board[r-inARow][c] = 125
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= 125:
                        copied_board[r+1][c] = 125
                if inARow == 4:
                    if r - inARow >= 0 and (copied_board[r-inARow][c] != 1 and copied_board[r-inARow][c] != 2) and copied_board[r-inARow][c] <= 550:
                        copied_board[r-inARow][c] = 550
                    if r + 1 < ROWS and (copied_board[r + 1][c] != 1 and copied_board[r+1][c] != 2) and copied_board[r+1][c] <= 550:
                        copied_board[r+1][c] = 550

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
                    if inARow == 2:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= 20:
                            copied_board[r-inARow][c-inARow] = 20
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= 20:
                            copied_board[r+1][c+1] = 20
                    if inARow == 3:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= 125:
                            copied_board[r-inARow][c-inARow] = 125
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= 125:
                            copied_board[r+1][c+1] = 125
                    if inARow == 4:
                        if r - inARow >= 0 and c-inARow >= 0 and (copied_board[r-inARow][c-inARow] != 1 and copied_board[r-inARow][c-inARow] != 2) and copied_board[r-inARow][c-inARow] <= 550:
                            copied_board[r-inARow][c-inARow] = 550
                        if r + 1 < ROWS and c+1 < COLUMNS and (copied_board[r+1][c+1] != 1 and copied_board[r+1][c+1] != 2) and copied_board[r+1][c+1] <= 550:
                            copied_board[r+1][c+1] = 550

        copied_board = np.rot90(copied_board, -2)     # Reverses the rotation to get back to the orginal orientation     
        # print(copied_board)    
        # Makes use of a boolean mask to make sure 1's and 2's are not included in the sum
        bmask = np.where((copied_board != 1)&(copied_board!= 2)) 
        maxSum = np.sum(copied_board[bmask])
        # print("maxSum = " + str(maxSum))
        # Calculates the score for the board by taking the score for Min away from the score for Max
        boardScore = maxSum - minSum
        return boardScore

    # Places a piece on the board
    def place_piece(self, move, player):
        row, column = move
        self.board[row, column] = player
    
    # Used by minimax to place a piece on the copied board
    def placePiece(self, board, move, player):
        row, column = move
        board[row, column] = player

    # Displays the winner of the game on the pygame window
    def display_winner(self, isWon, player):
        if isWon:
            font = pygame.font.Font(None, 36) # Default font
            textSurf = font.render(f"Player {player} wins!!", 1, BLACK)
            textRect = textSurf.get_rect(center=(WIDTH//2, HEIGHT//GRID_SIZE))  # Position the winning message
            self.WINDOW.blit(textSurf, textRect)  # Draws message on window 
            pygame.display.flip()
                        
    # Checks to see if the game has been won after that player plays a move
    def check_if_winner(self, player):
        self.check_if_draw(self.board, False)
        # Check for horizontal or vertical win
        def check_horizontalAndVertical(board, player):
            isWon = False
            for i in range(2):
                board = np.rot90(board, i)    # rotates the board counter-clockwise i times
                for r in range(ROWS):
                    inARow = 0
                    for c in range(COLUMNS):
                        if board[r][c] == player:
                            inARow += 1
                            if inARow == WIN_NUMBER:
                                self.display_winner(True, player)
                                print("Player " + str(player) + " has won!!")
                                return True
                        else:
                            inARow = 0
            return isWon
        
         # Checks for a postive or negative diagonal win 
        def check_diagonals(board, player):
            isWon = False
            for i in range(0,4):
                board = np.rot90(board, i)      # Makes use of numpy's function rot90 to check different diagonals
                r = ROWS
                c = 0
                for r in range(r, -1, -1):
                    inARow = 0
                    for r, c in zip(range(r, ROWS, 1), range(COLUMNS)):   # Uses 'zip' to put the column and row indexes together to form coordinates
                        if board[r][c] == player:
                            inARow += 1
                            if inARow == WIN_NUMBER:
                                self.display_winner(True, player)
                                print("Player " + str(player) + " has won!!")
                                return True
                        else: 
                            inARow = 0
            return isWon
        
        if check_horizontalAndVertical(self.board, player) :
            return True
        return check_diagonals(self.board, player)
    
    def checkWinner(self, board, player):
        # Check for horizontal or vertical win
        def check_horizontalAndVertical(board, player):
            isWon = False
            for i in range(2):
                board = np.rot90(board, i)
                for r in range(ROWS):
                    inARow = 0
                    for c in range(COLUMNS):
                        if board[r][c] == player:
                            inARow += 1
                            if inARow == WIN_NUMBER:
                                return True
                        else:
                            inARow = 0
            return isWon
        
         # Checks for a postive or negative diagonal win 
        def check_diagonals(board, player):
            isWon = False
            for i in range(0,4):
                board = np.rot90(board, i)
                r = ROWS
                c = 0
                for r in range(r, -1, -1):
                    inARow = 0
                    for r, c in zip(range(r, ROWS, 1), range(COLUMNS)):   # Puts the column and row indexes together to form coordinates
                        if board[r][c] == player:
                            inARow += 1
                            if inARow == WIN_NUMBER:
                                return True
                        else: 
                            inARow = 0
            return isWon
        
        if check_horizontalAndVertical(board, player) :
            return True
        return check_diagonals(board, player)
    
    def check_if_draw(self, board, isWon):
        # If the game has not been won and there are no available moves left, return True (draw)
        return (not isWon) and (np.all(board != 0))     # Uses numpy 'all' to check if every value in the board array is full
    
    # This scores the board and returns the copied board(2d array) with the updated scores
    # In minimax the 2d array this returns is iterated through and keeps the coords where values are over 10.
    def potential_moves(self, board):
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
                    # print(copied_board)
                                
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
        # print(copied_board)    
                                
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
        return copied_board
