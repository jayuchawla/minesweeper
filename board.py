class Board:
    def __init__(self, boardSize) -> None:
        self.board = []
        self.boardSize = boardSize
    
    def setBoard(self):
        for _ in self.boardSize[0]:
            row = []
            for _ in self.boardSize[1]:
                piece = None
                row.append(piece)
            self.board.append(row)

    def getBoardSize(self):
        return self.boardSize

