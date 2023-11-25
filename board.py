from piece import Piece
from random import random

class Board:
    def __init__(self, boardSize, prob) -> None:
        self.board = []
        self.boardSize = boardSize
        self.prob = prob
        self.setBoard()

    def setBoard(self):
        for _ in range(self.boardSize[0]):
            row = []
            for _ in range(self.boardSize[1]):
                piece = Piece(random() < self.prob)
                row.append(piece)
            self.board.append(row)
    
    def getPiece(self, coordinates):
        return self.board[coordinates[0]][coordinates[1]];
    
    def getBoardSize(self):
        return self.boardSize
