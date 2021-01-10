import copy
import math
import random

import pygame

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


def can_move(row: float, col: float, key=True):
    if col == -1 or col == len(game_board[0]) or game_board[int(row)][int(col)] != 3 or \
            int(row) == 15 and int(col) in (13, 14) and key:
        return True
    return False


def reset():
    global game
    game.pacman = Pacman(26.0, 13.5)
    game.ghosts = [Blinky(14.0, 13.5), Pinky(17.0, 13.5), Clyde(17.0, 15.5), Inky(17.0, 11.5)]
    game.lives -= 1
    game.paused = True
    game.render()


def pause(time):
    cur = 0
    while not cur == time:
        cur += 1


class Game:
    def __init__(self):
        self.ghosts = [Blinky(14.0, 13.5), Pinky(17.0, 13.5), Clyde(17.0, 15.5), Inky(17.0, 11.5)]
        self.ghosts_frightened = False

        self.pacman = Pacman(26.0, 13.5)
        self.lives = 3
        self.points = 0

        self.score = 0
        self.high_score = 0

        self.berry = f"tile08{random.randrange(0, 6)}.png"
        self.berries_collected = []
        self.berry_state = [200, 400, False]
        self.berry_location = [20.0, 13.5]
        self.berry_score = 100

        self.paused = True
        self.level_timer = 0
        self.is_game_over = False
        self.game_over_counter = 0

    def check_surroundings(self):
        for ghost in self.ghosts:
            if self.touching_pacman(ghost.row, ghost.col) and not ghost.active_frightened:
                if self.lives > 1:
                    reset()
                else:
                    self.is_game_over = True
                    return

        if self.pacman.row % 1.0 == 0 and self.pacman.col % 1.0 == 0:
            if game_board[int(self.pacman.row)][int(self.pacman.col)] == 2:
                game_board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 10
                self.points += 1
            elif game_board[int(self.pacman.row)][int(self.pacman.col)] == 6:
                game_board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 50
                self.points += 5

                for ghost in self.ghosts:
                    if ghost.active:
                        ghost.active_frightened = True
                        ghost.speed = 1 / 2

        if self.touching_pacman(self.berry_location[0], self.berry_location[1]) \
                and not self.berry_state[2] and self.level_timer in range(self.berry_state[0],
                                                                          self.berry_state[1]):
            self.berry_state[2] = True
            self.score += self.berry_score
            self.berries_collected.append(self.berry)

        if self.score > self.high_score:
            self.high_score = self.score
            self.record_high_score()

        if self.points == 260:
            # self.win
            pass

    def touching_pacman(self, row: float, col: float):
        if row - 0.5 <= self.pacman.row <= row and col == self.pacman.col:
            return True
        elif row + 0.5 >= self.pacman.row >= row and col == self.pacman.col:
            return True
        elif row == self.pacman.row and col - 0.5 <= self.pacman.col <= col:
            return True
        elif row == self.pacman.row and col + 0.5 >= self.pacman.col >= col:
            return True
        elif row == self.pacman.row and col == self.pacman.col:
            return True
        return False

    def started(self):
        self.paused = False

    def is_paused(self):
        return self.paused is True

    def game_over(self):
        global running
        if self.game_over_counter == 12:
            running = False
            self.record_high_score()
            return

        pacman_image = pygame.image.load(ELEMENT_PATH + "tile" +
                                         str(116 + self.game_over_counter) + ".png")
        pacman_image = pygame.transform.scale(pacman_image, (int(square * sprite_ratio),
                                                             int(square * sprite_ratio)))
        screen.blit(pacman_image, (self.pacman.col * square + sprite_offset,
                                   self.pacman.row * square + sprite_offset,
                                   square, square))
        pygame.display.update()
        pause(5000000)
        self.game_over_counter += 1

    def update(self):
        if self.is_game_over:
            self.game_over()
            return

        self.display_lives()
        self.display_score()
        self.display_collected_berries()
        self.draw_berry()
        self.check_surroundings()

        self.pacman.update()
        self.pacman.draw()

        for ghost in self.ghosts:
            ghost.update()
            ghost.draw()

        self.level_timer += 1

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

    def display_collected_berries(self):
        berry = [34, 26]
        for i in range(len(self.berries_collected)):
            image = pygame.image.load(ELEMENT_PATH + self.berries_collected[i])
            image = pygame.transform.scale(image, (
                int(square * sprite_ratio), int(square * sprite_ratio)))
            screen.blit(image, (
                (berry[1] - (2 * i)) * square, berry[0] * square + 5, square, square))

    def display_lives(self):
        location = [[34, 1], [34, 3]]
        for i in range(self.lives - 1):
            image = pygame.image.load(ELEMENT_PATH + "tile054.png")
            image = pygame.transform.scale(image, (int(square * sprite_ratio),
                                                   int(square * sprite_ratio)))
            screen.blit(image, (location[i][1] * square,
                                location[i][0] * square - sprite_offset,
                                square, square))

    def draw_berry(self):
        if self.level_timer in range(self.berry_state[0], self.berry_state[1]) \
                and not self.berry_state[2]:
            image = pygame.image.load(ELEMENT_PATH + self.berry)
            image = pygame.transform.scale(image, (
                int(square * sprite_ratio), int(square * sprite_ratio)))
            screen.blit(image, (
                self.berry_location[1] * square, self.berry_location[0] * square, square, square))

    def get_score(self):
        return self.score

    def get_points(self):
        return self.points

    def get_high_score(self):
        file = open(DATA_PATH + "high_score.txt", "r")
        self.high_score = int(file.read())
        file.close()

    def record_high_score(self):
        file = open(DATA_PATH + "high_score.txt", "w+")
        file.write(str(self.high_score))
        file.close()

    def render(self):
        screen.fill((0, 0, 0))

        self.display_score()
        self.display_lives()

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
                elif game_board[i][j] == 6:
                    pygame.draw.circle(screen, pellet_color,
                                       (j * square + square // 2, i * square + square // 2),
                                       square // 2)

                current_tile += 1
        pygame.display.update()


class Pacman:
    def __init__(self, row: float, col: float):
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
        if self.col < 0.5:
            self.col = 27.0
        if self.col > 27.0:
            self.col = 0

        if self.new_dir == 0:
            if can_move(math.floor(self.row - self.speed), self.col, key=False) \
                    and self.col % 1.0 == 0:
                self.row -= self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 1:
            if can_move(self.row, math.ceil(self.col + self.speed), key=False) \
                    and self.row % 1.0 == 0:
                self.col += self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 2:
            if can_move(math.ceil(self.row + self.speed), self.col, key=False) \
                    and self.col % 1.0 == 0:
                self.row += self.speed
                self.dir = self.new_dir
                return
        elif self.new_dir == 3:
            if can_move(self.row, math.floor(self.col - self.speed), key=False)\
                    and self.row % 1.0 == 0:
                self.col -= self.speed
                self.dir = self.new_dir
                return

        if self.dir == 0:
            if can_move(math.floor(self.row - self.speed), self.col, key=False) \
                    and self.col % 1.0 == 0:
                self.row -= self.speed
        elif self.dir == 1:
            if can_move(self.row, math.ceil(self.col + self.speed), key=False) \
                    and self.row % 1.0 == 0:
                self.col += self.speed
        elif self.dir == 2:
            if can_move(math.ceil(self.row + self.speed), self.col, key=False) \
                    and self.col % 1.0 == 0:
                self.row += self.speed
        elif self.dir == 3:
            if can_move(self.row, math.floor(self.col - self.speed), key=False) \
                    and self.row % 1.0 == 0:
                self.col -= self.speed

    # метод для рисования пакман в зависимости от его состояния
    def draw(self):
        if game.is_paused():
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
    SPRITES = []

    SPRITE_FRIGHTENED = pygame.image.load(ELEMENT_PATH + "tile072.png")
    SPRITE_FRIGHTENED_WHITE = pygame.image.load(ELEMENT_PATH + 'tile070.png')

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 0
        self.active = True
        self.active_scatter = False  # рассеивание
        self.active_frightened = False  # испуг
        self.calculate_ticks = False
        self.key_leave_home = True

    def update(self):
        self.change_active()
        if self.active:
            self.change_loc()
            self.change_direction()

            if self.move():
                return

            self.move()

    def change_active_scatter(self):
        self.active_scatter = True
        self.active_frightened = False

    def change_active_frightened(self):
        self.active_frightened = True
        self.active_scatter = False

    def change_activities(self):
        self.active_scatter = False
        self.active_frightened = False

    def transform_sprite(self):
        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))

    def draw(self):
        global start_ticks
        if not self.active_frightened:
            self.image = self.SPRITES[0]
            self.transform_sprite()
            if not self.active_frightened:
                if self.dir == 0:
                    self.image = self.SPRITES[0]
                elif self.dir == 1:
                    self.image = self.SPRITES[1]
                elif self.dir == 2:
                    self.image = self.SPRITES[2]
                elif self.dir == 3:
                    self.image = self.SPRITES[3]

            self.transform_sprite()

        elif self.active_frightened:
            self.transform_sprite()
            if not self.calculate_ticks:
                start_ticks = pygame.time.get_ticks()
                self.calculate_ticks = True
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if 4.0 < seconds < 7.0:
                if int(seconds) % 2 == 0:
                    self.image = self.SPRITE_FRIGHTENED_WHITE
                else:
                    self.image = self.SPRITE_FRIGHTENED
            elif seconds >= 7.0:
                self.active_frightened = False
                self.calculate_ticks = False
                self.speed = 1 / 2
            else:
                self.image = self.SPRITE_FRIGHTENED
            self.transform_sprite()

    def change_direction(self):
        pass

    def change_loc(self):
        if self.col < 0.5:
            self.col = 27.0

        if self.col > 27.0:
            self.col = 0.5

    def choose_direction_in_frightened(self):
        if self.dir == 0:
            self.random_choose_direction([0, 1, 3])

        elif self.dir == 1:
            self.random_choose_direction([0, 1, 2])

        elif self.dir == 2:
            self.random_choose_direction([1, 2, 3])

        elif self.dir == 3:
            self.random_choose_direction([0, 2, 3])

    def turn_in_impasse(self, moved):
        if not moved:
            if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home) \
                    and self.col % 1.0 == 0 \
                    and 2 != self.dir:
                self.dir = 0
            elif can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and 3 != self.dir:
                self.dir = 1
            elif can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home)\
                    and self.col % 1.0 == 0 \
                    and 0 != self.dir:
                self.dir = 2
            elif can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and 1 != self.dir:
                self.dir = 3

    def random_choose_direction(self, directions):
        direction = random.choice(directions)
        if self.can_move_in_this_dir(direction):
            self.dir = direction
        else:
            directions.remove(direction)
            direction = random.choice(directions)
            if self.can_move_in_this_dir(direction):
                self.dir = direction
            else:
                directions.remove(direction)
                if self.can_move_in_this_dir(directions[0]):
                    self.dir = directions[0]

    def can_move_in_this_dir(self, direction):
        if direction == 0:
            if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home)\
                    and self.col % 1.0 == 0 \
                    and 2 != self.dir:
                return True
        elif direction == 1:
            if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and 3 != self.dir:
                return True
        elif direction == 2:
            if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home)\
                    and self.col % 1.0 == 0 \
                    and 0 != self.dir:
                return True
        elif direction == 3:
            if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and self.dir != 1:
                return True

        return False

    def move(self):
        moved = False
        if self.dir == 0:
            if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home)\
                    and self.col % 1.0 == 0 \
                    and 2 != self.dir:
                self.row -= self.speed
                moved = True
        elif self.dir == 1:
            if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and 3 != self.dir:
                self.col += self.speed
                moved = True
        elif self.dir == 2:
            if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home)\
                    and self.col % 1.0 == 0 \
                    and 0 != self.dir:
                self.row += self.speed
                moved = True
        elif self.dir == 3:
            if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home)\
                    and self.row % 1.0 == 0 \
                    and self.dir != 1:
                self.col -= self.speed
                moved = True

        self.turn_in_impasse(moved)

        return moved

    def change_active(self):
        pass

    def leave_home(self):
        pass


class Blinky(Ghost):
    SPRITES = [pygame.image.load(ELEMENT_PATH + "tile102.png"),
               pygame.image.load(ELEMENT_PATH + "tile096.png"),
               pygame.image.load(ELEMENT_PATH + "tile098.png"),
               pygame.image.load(ELEMENT_PATH + "tile100.png")]

    def __init__(self, row, col):
        super(Ghost, self).__init__()
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 1  # 0: вверх, 1: вправо, 2: вниз, 3: влево
        self.active = True
        self.active_scatter = False
        self.active_frightened = False
        self.calculate_ticks = False
        self.key_leave_home = False

    def change_direction(self):
        if not self.active_frightened:
            if not self.active_scatter:
                vector = (self.col - game.pacman.col, self.row - game.pacman.row)

            else:
                vector = (self.col - 26.0, self.row - 6.0)

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
                    if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home) \
                            and self.row % 1.0 == 0 and 3 != self.dir:
                        self.dir = 1
                elif dir_pacman_hor == 'l':
                    if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home) \
                            and self.row % 1.0 == 0 and 1 != self.dir:
                        self.dir = 3
            else:
                if dir_pacman_ver == 'b':
                    if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home) \
                            and self.col % 1.0 == 0 and 0 != self.dir:
                        self.dir = 2
                elif dir_pacman_ver == 't':
                    if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home) \
                            and self.col % 1.0 == 0 and 2 != self.dir:
                        self.dir = 0

        else:
            self.choose_direction_in_frightened()


class Pinky(Ghost):
    SPRITES = [pygame.image.load(ELEMENT_PATH + "tile134.png"),
               pygame.image.load(ELEMENT_PATH + "tile128.png"),
               pygame.image.load(ELEMENT_PATH + "tile130.png"),
               pygame.image.load(ELEMENT_PATH + "tile132.png")]

    def __init__(self, row, col):
        super(Ghost, self).__init__()
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 0
        self.active = False
        self.active_scatter = False
        self.active_frightened = False
        self.calculate_ticks = False
        self.key_leave_home = True

    def change_active(self):
        self.active = True

    def leave_home(self):
        self.dir = 0
        if self.col >= 13.5 and self.row <= 14.0:
            self.key_leave_home = False

    def change_direction(self):
        if not self.active_frightened:
            if not self.key_leave_home:
                pacman_dir = game.pacman.dir
                if not self.active_scatter:
                    if pacman_dir == 0:
                        vector = (self.col - game.pacman.col, self.row - game.pacman.row + 2.5)
                    elif pacman_dir == 1:
                        vector = (self.col - game.pacman.col + 2.5, self.row - game.pacman.row)
                    elif pacman_dir == 2:
                        vector = (self.col - game.pacman.col, self.row - game.pacman.row - 2.5)
                    elif pacman_dir == 3:
                        vector = (self.col - game.pacman.col - 2.5, self.row - game.pacman.row)

                else:
                    vector = (self.col - 4.0, self.row - 6.0)

                if vector[0] < 0:
                    dir_hor = 'r'
                elif vector[0] > 0:
                    dir_hor = 'l'
                else:
                    dir_hor = ''

                if vector[1] < 0:
                    dir_ver = 'b'
                elif vector[1] > 0:
                    dir_ver = 't'
                else:
                    dir_ver = ''

                if game.ghosts[0].row == self.row:
                    if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home)\
                            and self.row % 1.0 == 0 \
                            and 3 != self.dir:
                        self.dir = 1
                        return
                    elif can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home)\
                            and self.row % 1.0 == 0 \
                            and self.dir != 1:
                        self.dir = 3
                        return
                elif game.ghosts[0].col == self.col:
                    if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home)\
                            and self.col % 1.0 == 0 \
                            and 2 != self.dir:
                        self.dir = 0
                        return
                    elif can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home)\
                            and self.col % 1.0 == 0 \
                            and 0 != self.dir:
                        self.dir = 2
                        return

                if self.dir % 2 != 0:
                    if dir_ver == 't':
                        if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home) \
                                and self.col % 1.0 == 0 and 2 != self.dir:
                            self.dir = 0
                            return
                    elif dir_ver == 'b':
                        if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home) \
                                and self.col % 1.0 == 0 and 0 != self.dir:
                            self.dir = 2
                            return
                else:
                    if dir_hor == 'l':
                        if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home) \
                                and self.row % 1.0 == 0 and 1 != self.dir:
                            self.dir = 3
                            return
                    elif dir_hor == 'r':
                        if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home) \
                                and self.row % 1.0 == 0 and 3 != self.dir:
                            self.dir = 1
                            return
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


class Inky(Ghost):
    SPRITES = [pygame.image.load(ELEMENT_PATH + "tile142.png"),
               pygame.image.load(ELEMENT_PATH + "tile136.png"),
               pygame.image.load(ELEMENT_PATH + "tile138.png"),
               pygame.image.load(ELEMENT_PATH + "tile140.png")]

    def __init__(self, row, col):
        super(Ghost, self).__init__()
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 0
        self.active = False
        self.active_scatter = False
        self.active_frightened = False
        self.calculate_ticks = False
        self.key_leave_home = True

    def change_active(self):
        if game.get_points() >= 30:
            self.active = True

    def leave_home(self):
        print(self.col, self.row)
        if self.row >= 14.0:
            self.dir = 0
        else:
            self.dir = 1
        if self.col >= 13.5 and self.row <= 14.0:
            self.key_leave_home = False

    def change_direction(self):
        if not self.active_frightened:
            if not self.key_leave_home:
                if not self.active_scatter:
                    vector = [game.ghosts[0].col - game.pacman.col,
                              game.ghosts[0].row - game.pacman.row]
                    pacman_dir = game.pacman.dir
                    if pacman_dir == 0:
                        vector[1] += 1.0
                    elif pacman_dir == 1:
                        vector[1] += 1.0
                    elif pacman_dir == 2:
                        vector[0] -= 1.0
                    elif pacman_dir == 3:
                        vector[0] -= 1.0

                    vector = [vector[0] * 2 + game.ghosts[0].col, vector[0] * 2 + game.ghosts[0].row]

                else:
                    vector = [self.col - 7.0, self.row - 30.0]

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
                        if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home)\
                                and self.row % 1.0 == 0 \
                                and 3 != self.dir:
                            self.dir = 1
                    elif dir_pacman_hor == 'l':
                        if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home) \
                                and self.row % 1.0 == 0 and 1 != self.dir:
                            self.dir = 3
                else:
                    if dir_pacman_ver == 'b':
                        if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home) \
                                and self.col % 1.0 == 0 and 0 != self.dir:
                            self.dir = 2
                    elif dir_pacman_ver == 't':
                        if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home) \
                                and self.col % 1.0 == 0 and 2 != self.dir:
                            self.dir = 0
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


class Clyde(Ghost):
    SPRITES = [pygame.image.load(ELEMENT_PATH + "tile150.png"),
               pygame.image.load(ELEMENT_PATH + "tile144.png"),
               pygame.image.load(ELEMENT_PATH + "tile146.png"),
               pygame.image.load(ELEMENT_PATH + "tile148.png")]

    def __init__(self, row, col):
        super(Ghost, self).__init__()
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 1  # 0: вверх, 1: вправо, 2: вниз, 3: влево
        self.active = False
        self.active_scatter = False
        self.active_frightened = False
        self.calculate_ticks = False
        self.key_leave_home = True

    def change_active(self):
        if game.get_points() >= 80:
            self.active = True

    def leave_home(self):
        print(self.row, self.col)
        if self.col >= 13.5:
            self.dir = 3
        else:
            self.dir = 0

        if self.col == 13.5 and self.row == 14.0:
            self.key_leave_home = False

    def change_direction(self):
        if not self.active_frightened:
            if not self.key_leave_home:
                if not self.active_scatter:
                    if self.dir == 0:
                        self.random_choose_direction([0, 1, 3])

                    elif self.dir == 1:
                        self.random_choose_direction([0, 1, 2])

                    elif self.dir == 2:
                        self.random_choose_direction([1, 2, 3])

                    elif self.dir == 3:
                        self.random_choose_direction([0, 2, 3])

                else:
                    vector = (self.col - 19.0, self.row - 30.0)

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
                            if can_move(self.row,
                                        math.ceil(self.col + self.speed)) and self.row % 1.0 == 0 \
                                    and 3 != self.dir:
                                self.dir = 1
                        elif dir_pacman_hor == 'l':
                            if can_move(self.row,
                                        math.floor(self.col - self.speed)) and self.row % 1.0 == 0 \
                                    and 1 != self.dir:
                                self.dir = 3
                    else:
                        if dir_pacman_ver == 'b':
                            if can_move(math.ceil(self.row + self.speed),
                                        self.col) and self.col % 1.0 == 0 \
                                    and 0 != self.dir:
                                self.dir = 2
                        elif dir_pacman_ver == 't':
                            if can_move(math.floor(self.row - self.speed),
                                        self.col) and self.col % 1.0 == 0 \
                                    and 2 != self.dir:
                                self.dir = 0
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


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
