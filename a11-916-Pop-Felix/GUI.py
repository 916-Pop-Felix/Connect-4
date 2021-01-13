import pygame
import sys
import math

CIRCLE_SIZE = 100
RADIUS = int(CIRCLE_SIZE / 2 - 5)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


class GUI:
    def __init__(self, service, lines, columns):

        self.__service = service
        self.lines = lines
        self.columns = columns
        self.width = columns * CIRCLE_SIZE
        self.height = lines * CIRCLE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True

    def run_app(self):
        pygame.init()
        pygame.display.set_caption("Connect4")
        turn = "human"
        font = pygame.font.SysFont("monospace", 50)
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                self.draw_board()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, CIRCLE_SIZE))
                    pos = event.pos[0]
                    if turn == "human":
                        pygame.draw.circle(self.screen, RED, (pos, int(CIRCLE_SIZE / 2)), RADIUS)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, CIRCLE_SIZE))
                    if turn == "human":
                        pos = event.pos[0]
                        col = int(math.floor(pos / CIRCLE_SIZE))
                        try:
                            self.__service.move(col + 1, "human")
                            turn = "cpu"
                            if self.__service.check_winner("human"):
                                label = font.render("Congratulations! You've won!", 1, RED)
                                self.screen.blit(label, (40, 10))
                                self.running = False

                        except ValueError as ve:
                            label = font.render(str(ve), 1, RED)
                            self.screen.blit(label, (40, 10))
                        self.draw_board()
            if turn == "cpu" and self.running:
                pygame.time.wait(1000)
                self.__service.cpu_move(1)
                turn = "human"
                if self.__service.check_winner("cpu"):
                    label = font.render("You lost! Maybe try harder next time :)", 1, RED)
                    self.screen.blit(label, (40, 10))
                    self.running = False
                self.draw_board()
            if not self.running:
                pygame.time.wait(5000)

    def draw_board(self):
        for c in range(self.columns):
            for r in range(self.lines):
                pygame.draw.rect(self.screen, BLUE,
                                 (c * CIRCLE_SIZE, r * CIRCLE_SIZE + CIRCLE_SIZE, CIRCLE_SIZE, CIRCLE_SIZE))
                pygame.draw.circle(self.screen, BLACK, (
                    int(c * CIRCLE_SIZE + CIRCLE_SIZE / 2), int(r * CIRCLE_SIZE + CIRCLE_SIZE + CIRCLE_SIZE / 2)),
                                   RADIUS)

        for c in range(self.columns):
            for r in range(self.lines):
                if self.__service.board().board[r][c].player == "human":
                    pygame.draw.circle(self.screen, RED, (
                        int(c * CIRCLE_SIZE + CIRCLE_SIZE / 2), int(r * CIRCLE_SIZE + CIRCLE_SIZE / 2)), RADIUS)
                elif self.__service.board().board[r][c].player == "cpu":
                    pygame.draw.circle(self.screen, YELLOW, (
                        int(c * CIRCLE_SIZE + CIRCLE_SIZE / 2), int(r * CIRCLE_SIZE + CIRCLE_SIZE / 2)), RADIUS)
        pygame.display.update()
