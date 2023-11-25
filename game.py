import os
import pygame

class Game:
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getBoardSize()[1], self.screenSize[1] // self.board.getBoardSize()[0]
        self.loadimages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=self.screenSize)
        running = True

        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        currentPosition = (0, 0)
        for rowIndex in range(self.board.getBoardSize()[0]):
            for colIndex in range(self.board.getBoardSize()[1]):
                piece = self.board.getPiece((rowIndex, colIndex))
                if piece.getHasBomb():
                    image = self.images["unclicked-bomb"]
                else:
                    image = self.images["empty-block"]
                self.screen.blit(image, currentPosition)
                currentPosition = (currentPosition[0] + self.pieceSize[0], currentPosition[1])
            currentPosition = (0, currentPosition[1] + self.pieceSize[1])

    def loadimages(self):
        self.images = dict()
        for fileName in os.listdir("static/images"):
            if not fileName.endswith(".png") and not fileName.endswith(".jpg"):
                continue
            image = pygame.image.load(os.path.join("static/images", fileName))
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image