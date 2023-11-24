from game import Game
from board import Board
board = Board((9,9))
screenSize = (400,400)
game = Game(board=board, screenSize=screenSize)
game.run()