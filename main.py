from game import Game
from board import Board
prob = 0.2
board = Board((9,9), prob=prob)
screenSize = (400,400)
game = Game(board=board, screenSize=screenSize)
game.run()