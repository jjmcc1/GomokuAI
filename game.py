# Author:    James McCafferty
# Created:   26.03.2024

from constants import PLAYER_1, PLAYER_2, ROWS, COLUMNS, WIDTH, HEIGHT, GRID_SIZE
from board import Board
import pygame
from minimax import minimax
import time

class Game:
    # Constructor
    def __init__(self):
        self.board = Board()    # Creates an instance of the board class
        self.player = PLAYER_1  # Initialises the player to be player 1
    # Changes the player (1 to 2) or (2 to 1)
    def switch_player(self):
        if self.player == PLAYER_1:
            self.player = PLAYER_2
        else:
            self.player = PLAYER_1 
    # Main game loop
    def game_loop(self):
        self.board.print_board()            # Prints board in terminal
        pygame.init()                       # Initialises pygame
        self.board.create_window()          # Creates pygame window
        self.board.draw_board()             # Draws gomoku board on window
        pygame.display.update()             # Updates the window

        isWon = False                       # isWon is initially set to False

        while not isWon:                                # While the game hasn't been won
            for event in pygame.event.get():            # Iterates over each event in the list returned by pygame.event.get()
                if event.type == pygame.QUIT:           # If someone presses the 'X' top right corner it will close
                    exit(0)   
                if event.type == pygame.MOUSEBUTTONDOWN:                # If the event is a mouse click on the screen
                    pos = pygame.mouse.get_pos()                        # Record the position of that click
                    x = pos[0]                                          # Store the x position  
                    y = pos[1]                                          # Store the y position
                    row = int((y - 0.5 * GRID_SIZE) // GRID_SIZE)       # Determine what row the click corresponds to
                    column = int((x - 0.5 * GRID_SIZE) // GRID_SIZE)    # Determine what column the click corresponds to
                    move = (row, column)                                # Combine the row and column to make a move
                    if self.board.is_pos_full(move) != True:            # If the position at those coords is free then place the piece there
                        self.board.place_piece(move, self.player)       
                        self.board.print_board()
                        self.board.draw_board()
                        isWon = self.board.check_if_winner(self.player) # Check if that move is a winning move or a drawing move
                        if isWon:                                       # If the move is a winner, then wait and end the game
                            pygame.time.wait(2000)
                            pygame.quit()
                            break
                        self.switch_player()                            # If still playing, switch the player
                        depth = 2  # Change this to adjust the depth (look-ahead)
                        # This is the line that calls minimax:
                        start = time.time()
                        evaluation, ai_move = minimax(self.board, self.board.board, depth, True)  # Calls the minimax function to get the AI move
                        self.board.place_piece(ai_move, self.player)                        # Places the ai's move on the screen
                        end = time.time()
                        print(end - start)
                        self.board.print_board()                                            # Prints the updated board in the terminal
                        self.board.draw_board()                                             # Draws the new board on the pygame window
                        isWon = self.board.check_if_winner(self.player)                     # Checks if that move was a winner for the AI or if it is a draw 
                        self.switch_player()                                                # Switches player back to human
                    if isWon:
                        pygame.time.wait(3000)    
        pygame.quit()
