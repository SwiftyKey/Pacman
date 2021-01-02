import copy
import math

import pygame
import random

BOARD_PATH = "resources/BoardTiles/"
TEXT_PATH = "resources/TextTiles/"
ELEMENT_PATH = "resources/OtherTiles/"
DATA_PATH = "resources/UserData/"

original_game_Board = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 6, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 6, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 6, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 6, 3],
    [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
    [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]
game_board = copy.deepcopy(original_game_Board)
square = 20

sprite_ratio = 3 / 2
sprite_offset = square * (1 - sprite_ratio) * (1 / 2)

(width, height) = (len(game_board[0]) * square, len(game_board) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pacman")
pellet_color = (222, 161, 133)

fps = 60
clock = pygame.time.Clock()
running = True


class Game:
    def __init__(self):
        self.pacman = Pacman(26.0, 13.5)
        self.ghost = Ghost(14.0, 13.5)
        self.points = []
        self.lives = 3

        self.score = 0
        self.high_score = 0

        self.paused = True

    def started(self):
        self.paused = False

    def is_paused(self):
        return self.paused is True

    def update(self):
        self.pacman.update()
        self.pacman.draw()
        self.ghost.update()
        self.ghost.draw()
        self.display_score()

    def display_score(self):
        text_one_up = ["tile033.png", "tile021.png", "tile016.png"]
        text_high_score = ["tile007.png", "tile008.png", "tile006.png", "tile007.png", "tile015.png",
                           "tile019.png", "tile002.png", "tile014.png", "tile018.png", "tile004.png"]
        index = 0
        score_start = 5
        high_score_start = 11
        for i in range(score_start, score_start + len(text_one_up)):
            image = pygame.image.load(TEXT_PATH + text_one_up[index])
            image = pygame.transform.scale(image, (square, square))
            screen.blit(image, (i * square, 4, square, square))
            index += 1
        score = str(self.score)
        if score == "0":
            score = "00"
        index = 0
        for i in range(0, len(score)):
            digit = int(score[i])
            image = pygame.image.load(TEXT_PATH + "tile0" + str(32 + digit) + ".png")
            image = pygame.transform.scale(image, (square, square))
            screen.blit(image, ((score_start + 2 + index) * square, square + 4, square, square))
            index += 1

        index = 0
        for i in range(high_score_start, high_score_start + len(text_high_score)):
            image = pygame.image.load(TEXT_PATH + text_high_score[index])
            image = pygame.transform.scale(image, (square, square))
            screen.blit(image, (i * square, 4, square, square))
            index += 1

        self.get_high_score()
        high_score = str(self.high_score)
        if high_score == "0":
            high_score = "00"
        index = 0
        for i in range(0, len(high_score)):
            digit = int(high_score[i])
            image = pygame.image.load(TEXT_PATH + "tile0" + str(32 + digit) + ".png")
            image = pygame.transform.scale(image, (square, square))
            screen.blit(image, ((high_score_start + 6 + index) * square, square + 4, square, square))
            index += 1

    def get_high_score(self):
        file = open(DATA_PATH + "high_score.txt", "r")
        self.high_score = int(file.read())
        file.close()

    def record_high_score(self):
        file = open(DATA_PATH + "HighScore.txt", "w+")
        file.write(str(self.high_score))
        file.close()

    @staticmethod
    def render():
        screen.fill((0, 0, 0))

        current_tile = 0
        for i in range(3, len(game_board) - 2):
            for j in range(len(game_board[0])):
                if game_board[i][j] == 3:
                    image = str(current_tile)
                    if len(image) == 1:
                        image = "00" + image
                    elif len(image) == 2:
                        image = "0" + image

                    image = "tile" + image + ".png"
                    tile = pygame.image.load(BOARD_PATH + image)
                    tile = pygame.transform.scale(tile, (square, square))

                    screen.blit(tile, (j * square, i * square, square, square))

                elif game_board[i][j] == 2:
                    pygame.draw.circle(screen, pellet_color,
                                       (j * square + square // 2, i * square + square // 2),
                                       square // 4)
                elif game_board[i][j] == 5:
                    pygame.draw.circle(screen, (0, 0, 0),
                                       (j * square + square // 2, i * square + square // 2),
                                       square // 2)
                elif game_board[i][j] == 6:
                    pygame.draw.circle(screen, pellet_color,
                                       (j * square + square // 2, i * square + square // 2),
                                       square // 2)

                current_tile += 1
        pygame.display.update()


class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mouth_open = False
        self.speed = 1 / 2
        self.mouth_change_delay = 5
        self.mouth_change_count = 0
        self.image = None
        self.dir = 0  # 0: вверх, 1: вправо, 2: вниз, 3: влево
        self.new_dir = 0

    def change_direction(self, new_dir: int):
        self.new_dir = new_dir

    def update(self):
        if self.new_dir == 0:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 1:
            if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 2:
            if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 3:
            if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed
                self.dir = self.new_dir
                return

        if self.dir == 0:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed

    # метод для рисования пакман в зависимости от его состояния
    def draw(self):
        self.image = pygame.image.load(ELEMENT_PATH + "tile112.png")
        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))

        if self.mouth_change_count == self.mouth_change_delay:
            self.mouth_change_count = 0
            self.mouth_open = not self.mouth_open
        self.mouth_change_count += 1

        if self.dir == 0:
            if self.mouth_open:
                self.image = pygame.image.load(ELEMENT_PATH + "tile049.png")
            else:
                self.image = pygame.image.load(ELEMENT_PATH + "tile051.png")
        elif self.dir == 1:
            if self.mouth_open:
                self.image = pygame.image.load(ELEMENT_PATH + "tile052.png")
            else:
                self.image = pygame.image.load(ELEMENT_PATH + "tile054.png")
        elif self.dir == 2:
            if self.mouth_open:
                self.image = pygame.image.load(ELEMENT_PATH + "tile053.png")
            else:
                self.image = pygame.image.load(ELEMENT_PATH + "tile055.png")
        elif self.dir == 3:
            if self.mouth_open:
                self.image = pygame.image.load(ELEMENT_PATH + "tile048.png")
            else:
                self.image = pygame.image.load(ELEMENT_PATH + "tile050.png")

        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))


class Ghost:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = random.choice([1, 3])  # 0: вверх, 1: вправо, 2: вниз, 3: влево
        self.new_dir = 0

    def update(self):
        self.change_direction()
        moved = False

        if self.dir == 0:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
                moved = True
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
                moved = True
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
                moved = True
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed
                moved = True

        self.turn_in_impasse(moved)

    def change_direction(self):
        vector = (self.col - game.pacman.col, self.row - game.pacman.row)
        if vector[0] < 0:
            dir_pacman_hor = 'r'
        elif vector[0] > 0:
            dir_pacman_hor = 'l'
        else:
            dir_pacman_hor = ''

        if vector[1] < 0:
            dir_pacman_ver = 'b'
        elif vector[1] > 0:
            dir_pacman_ver = 't'
        else:
            dir_pacman_ver = ''

        if self.dir % 2 == 0:
            if dir_pacman_hor == 'r':
                if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0 \
                        and 3 != self.dir:
                    self.dir = 1
            elif dir_pacman_hor == 'l':
                if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0 \
                        and 1 != self.dir:
                    self.dir = 3
        else:
            if dir_pacman_ver == 'b':
                if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0 \
                        and 0 != self.dir:
                    self.dir = 2
            elif dir_pacman_ver == 't':
                if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0 \
                        and 2 != self.dir:
                    self.dir = 0

    def turn_in_impasse(self, moved):
        if moved == False:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0 \
                    and 0 != self.dir:
                self.dir = 0
            elif canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0 \
                    and 1 != self.dir:
                self.dir = 1
            elif canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0 \
                    and 2 != self.dir:
                self.dir = 2
            elif canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0 \
                    and 3 != self.dir:
                self.dir = 3

    def draw(self):
        self.image = pygame.image.load(ELEMENT_PATH + "tile096.png")
        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))
        if self.dir == 0:
            self.image = pygame.image.load(ELEMENT_PATH + "tile102.png")
        elif self.dir == 1:
            self.image = pygame.image.load(ELEMENT_PATH + 'tile096.png')
        elif self.dir == 2:
            self.image = pygame.image.load(ELEMENT_PATH + 'tile098.png')
        elif self.dir == 3:
            self.image = pygame.image.load(ELEMENT_PATH + 'tile100.png')

        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))


def canMove(row: int, col: int):
    if col == -1 or col == len(game_board[0]) or game_board[int(row)][int(col)] != 3:
        return True
    return False


game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            game.started()
            if event.key == pygame.K_w:
                game.pacman.change_direction(0)
            elif event.key == pygame.K_d:
                game.pacman.change_direction(1)
            elif event.key == pygame.K_s:
                game.pacman.change_direction(2)
            elif event.key == pygame.K_a:
                game.pacman.change_direction(3)
    game.render()
    if not game.is_paused():
        game.update()
    pygame.display.flip()
    clock.tick(fps)
