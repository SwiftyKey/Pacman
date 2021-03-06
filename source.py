import copy
import math
import random

import pygame

# пути к ресурсам
BOARD_PATH = "resources/BoardTiles/"
TEXT_PATH = "resources/TextTiles/"
ELEMENT_PATH = "resources/OtherTiles/"
DATA_PATH = "resources/UserData/"
MUSIC_PATH = "resources/Music/"

# исходная карта
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
# карта для игры
game_board = copy.deepcopy(original_game_Board)
# размер клетки
square = 20

# соотношение спрайтов
sprite_ratio = 3 / 2
# смещение
sprite_offset = square * (1 - sprite_ratio) * (1 / 2)

# размеры окна
(width, height) = (len(game_board[0]) * square, len(game_board) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pacman")
# цветовая палитра клеток
pellet_color = (222, 161, 133)

# количество кадров в секунду
fps = 60
# переменная для сохранение количества тиков для испуга у призраков
start_ticks = 0
clock = pygame.time.Clock()
# флаг для старта программы
running = True
# флаг для старта новой игры
new_game = False

pygame.mixer.init()


def find_direction(vector: list):  # функция для определения положения точки, относительно призрака
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

    return dir_hor, dir_ver


# функция для проверки возможности пойти в какую-то клетку
def can_move(row: float, col: float, key=True):
    if col == -1 or col == len(game_board[0]) or game_board[int(row)][int(col)] != 3 or \
            int(row) == 15 and int(col) in (13, 14) and key:
        return True
    return False


# функция для остановки на какое-то время
def pause(time: int):
    cur = 0
    while not cur == time:
        cur += 1


# функция для прогирывания музыки
def play_music(music: str, force=False):
    if force:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(MUSIC_PATH + music)
        pygame.mixer.music.play()
    else:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
            pygame.mixer.music.load(MUSIC_PATH + music)
            pygame.mixer.music.queue(MUSIC_PATH + music)
            pygame.mixer.music.play()


# функция для построения заставки игры
def splash_screen():
    pacman_title = ["tile016.png", "tile000.png", "tile448.png", "tile012.png", "tile000.png",
                    "tile013.png"]
    for i in range(len(pacman_title)):
        letter = pygame.image.load(TEXT_PATH + pacman_title[i])
        letter = pygame.transform.scale(letter, (int(square * 4), int(square * 4)))
        screen.blit(letter, ((2 + 4 * i) * square, 2 * square, square, square))

    character_title = [
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png",
        "tile020.png", "tile004.png", "tile018.png",

        "tile015.png", "tile042.png", "tile015.png",

        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png",
        "tile012.png", "tile004.png"
    ]
    for i in range(len(character_title)):
        letter = pygame.image.load(TEXT_PATH + character_title[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4 + i) * square, 10 * square, square, square))

    characters = [
        [
            "tile449.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png",
            "tile064.png", "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png",
            "tile089.png", "tile108.png"
        ],
        [
            "tile450.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png",
            "tile324.png", "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png",
            "tile364.png"
        ],
        [
            "tile452.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png",
            "tile211.png", "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        [
            "tile451.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png",
            "tile266.png", "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png",
            "tile300.png"
        ]
    ]
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if j == 0:
                letter = pygame.image.load(TEXT_PATH + characters[i][j])
                letter = pygame.transform.scale(letter, (
                    int(square * sprite_ratio), int(square * sprite_ratio)))
                screen.blit(letter, (
                    (2 + j) * square - square // 2, (12 + 2 * i) * square - square // 3, square,
                    square))
            else:
                letter = pygame.image.load(TEXT_PATH + characters[i][j])
                letter = pygame.transform.scale(letter, (int(square), int(square)))
                screen.blit(letter, ((2 + j) * square, (12 + 2 * i) * square, square, square))

    event = ["tile449.png", "tile015.png", "tile452.png", "tile015.png", "tile015.png",
             "tile448.png", "tile453.png", "tile015.png", "tile015.png", "tile015.png",
             "tile453.png"]
    for i in range(len(event)):
        character = pygame.image.load(TEXT_PATH + event[i])
        character = pygame.transform.scale(character, (int(square * 2), int(square * 2)))
        screen.blit(character, ((4 + i * 2) * square, 24 * square, square, square))

    wall = ["tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png",
            "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png",
            "tile454.png", "tile454.png", "tile454.png"]
    for i in range(len(wall)):
        platform = pygame.image.load(TEXT_PATH + wall[i])
        platform = pygame.transform.scale(platform, (int(square * 2), int(square * 2)))
        screen.blit(platform, ((i * 2) * square, 26 * square, square, square))

    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png",
                    "tile015.png", "tile019.png", "tile016.png", "tile000.png", "tile002.png",
                    "tile004.png", "tile015.png", "tile020.png", "tile014.png", "tile015.png",
                    "tile016.png", "tile011.png", "tile000.png", "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(TEXT_PATH + instructions[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4.5 + i) * square, 32 * square - 10, square, square))

    pygame.display.update()


# класс игры
class Game:
    POINTS = 260

    def __init__(self, levels: int = 1):
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
        self.levels = levels
        self.cur_level = 1
        self.is_game_over = False
        self.is_win = False
        self.game_over_counter = 0

    # метод для проверки взаимодействия объектов с пакманом
    def check_surroundings(self):
        global start_ticks, game_board, original_game_Board

        for ghost in self.ghosts:
            if self.touching_pacman(ghost.row, ghost.col) and not ghost.active_frightened:
                if self.lives > 1:
                    self.reset()
                    play_music("pacman_death.wav", True)
                    return
                else:
                    self.is_game_over = True
                    play_music("death_1.wav", True)
                    return

        if self.pacman.row % 1.0 == 0 and self.pacman.col % 1.0 == 0:
            if game_board[int(self.pacman.row)][int(self.pacman.col)] == 2:
                game_board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 10
                self.points += 1
                play_music("munch_1.wav")
            elif game_board[int(self.pacman.row)][int(self.pacman.col)] == 6:
                game_board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 50
                self.points += 5

                for ghost in self.ghosts:
                    if ghost.active:
                        ghost.active_frightened = True
                        ghost.speed = 1 / 2

                play_music("power_pellet.wav", True)

        if self.touching_pacman(self.berry_location[0], self.berry_location[1]) \
                and not self.berry_state[2] and self.level_timer in range(self.berry_state[0],
                                                                          self.berry_state[1]):
            self.berry_state[2] = True
            self.score += self.berry_score
            self.berries_collected.append(self.berry)
            play_music("eat_fruit.wav", True)

        if self.score > self.high_score:
            self.high_score = self.score
            self.record_high_score()

        if self.points == self.POINTS and self.cur_level == self.levels:
            self.is_win = True
            play_music("intermission.wav", True)
            return
        elif self.points == self.POINTS and self.cur_level < self.levels:
            game_board = copy.deepcopy(original_game_Board)
            play_music("intermission.wav")
            self.new_level()
            play_music("game_start")
            return

    # метод для проверки возможности касания пакмана
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

    # метод для установки флага старта игры на True
    def started(self):
        self.paused = False

    # метод для проверки на остановку игры
    def is_paused(self):
        return self.paused is True

    # метод для окончания игры и начала новой
    def game_over(self):
        global new_game
        if self.game_over_counter == 12:
            new_game = True
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

    # метод для победы и начала новой игры
    @staticmethod
    def win():
        global new_game

        new_game = True
        return

    # метод для начала игры с новой жизни
    def reset(self):
        self.pacman = Pacman(26.0, 13.5)
        self.ghosts = [Blinky(14.0, 13.5), Pinky(17.0, 13.5), Clyde(17.0, 15.5), Inky(17.0, 11.5)]
        self.lives -= 1
        self.paused = True
        self.render()

    # метод для начала нового уровня
    def new_level(self):
        self.reset()
        self.lives += 1
        self.cur_level += 1
        self.berries_collected = []
        self.berry = f"tile08{random.randrange(0, 6)}.png"
        self.points = 0

    # метод для обновления экрана игры
    def update(self):
        if self.is_game_over:
            self.game_over()
            return

        if self.is_win:
            self.win()
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

    # метод для отображения количества собранных очнов
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

    # метод для отображения собранных ягод
    def display_collected_berries(self):
        berry = [34, 26]
        for i in range(len(self.berries_collected)):
            image = pygame.image.load(ELEMENT_PATH + self.berries_collected[i])
            image = pygame.transform.scale(image, (
                int(square * sprite_ratio), int(square * sprite_ratio)))
            screen.blit(image, (
                (berry[1] - (2 * i)) * square, berry[0] * square + 5, square, square))

    # метод для отображения количества жизней
    def display_lives(self):
        location = [[34, 1], [34, 3]]
        for i in range(self.lives - 1):
            image = pygame.image.load(ELEMENT_PATH + "tile054.png")
            image = pygame.transform.scale(image, (int(square * sprite_ratio),
                                                   int(square * sprite_ratio)))
            screen.blit(image, (location[i][1] * square,
                                location[i][0] * square - sprite_offset,
                                square, square))

    # метод для рисовки ягод
    def draw_berry(self):
        if self.level_timer in range(self.berry_state[0], self.berry_state[1]) \
                and not self.berry_state[2]:
            image = pygame.image.load(ELEMENT_PATH + self.berry)
            image = pygame.transform.scale(image, (
                int(square * sprite_ratio), int(square * sprite_ratio)))
            screen.blit(image, (
                self.berry_location[1] * square, self.berry_location[0] * square, square, square))

    # метод для получения количества съеденых точек
    def get_points(self):
        return self.points

    # метод для получения лучшего рекорда
    def get_high_score(self):
        file = open(DATA_PATH + "high_score.txt", "r")
        self.high_score = int(file.read())
        file.close()

    # метод для записи нового рекорда
    def record_high_score(self):
        file = open(DATA_PATH + "high_score.txt", "w+")
        file.write(str(self.high_score))
        file.close()

    # метод для рисовки поля
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


# класс для пакмана
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

    # метод для изменения направления движения
    def change_direction(self, new_dir: int):
        self.new_dir = new_dir

    # метод для обновления модели пакмана на экране
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
            if can_move(self.row, math.floor(self.col - self.speed), key=False) \
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

    # метод для рисования пакмана в зависимости от его состояния
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


class Ghost:  # родительский класс для всех призраков, в котором хранятся основные методы
    SPRITES = []  # список спрайтов для призраков

    SPRITE_FRIGHTENED = pygame.image.load(ELEMENT_PATH + "tile072.png")  # спрайт,
    # когда призрак испуган
    SPRITE_FRIGHTENED_WHITE = pygame.image.load(ELEMENT_PATH + 'tile070.png')  # спрайт,

    # когда призрак испуган, только белый

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.speed = 1 / 2
        self.image = None
        self.dir = 0  # 0: вверх, 1: вправо, 2: вниз, 3: влево
        self.active = True  # флаг, отвечающий за активность призрака
        self.active_scatter = False  # рассеивание
        self.active_frightened = False  # испуг
        self.calculate_ticks = False  # флаг, отвечающий за начало или конец подсчета тиков
        self.key_leave_home = True  # флаг, True если призраки в доме, False,
        # если призраки вышли из дома

    def update(self):  # метод для изменения положения призрака, изменения его активности и т.д.
        self.change_active()
        if self.active:
            self.change_loc()
            self.change_direction()

            if self.move():  # сделано для того, чтобы если призрак не движется,
                # то он менял свое направление
                return

            self.move()

    def change_active_scatter(self):  # для того, чтобы активировать разбегание, которое,
        # к сожалению, так и не было реализовано в игре :(
        self.active_scatter = True
        self.active_frightened = False

    def transform_sprite(self):  # функиця для трансформации спрайта
        self.image = pygame.transform.scale(self.image, (int(square * sprite_ratio),
                                                         int(square * sprite_ratio)))
        screen.blit(self.image, (self.col * square + sprite_offset,
                                 self.row * square + sprite_offset,
                                 square, square))

    def draw(self):  # метод рисования призраков, в зависимости от состояния
        global start_ticks
        if not self.active_frightened:  # рисуем в обычном состоянии
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

        elif self.active_frightened:  # рисуем в испуге
            self.transform_sprite()
            if not self.calculate_ticks:
                start_ticks = pygame.time.get_ticks()
                self.calculate_ticks = True
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if 3.0 < seconds < 6.0:  # в последние три секунды мигает
                if int(seconds) % 2 == 1:
                    self.image = self.SPRITE_FRIGHTENED_WHITE
                else:
                    self.image = self.SPRITE_FRIGHTENED
            elif seconds >= 6.0:
                self.active_frightened = False
                self.calculate_ticks = False
            else:
                self.image = self.SPRITE_FRIGHTENED
            self.transform_sprite()

    def change_direction(self):  # метод смены направления, разные для каждого призрака
        pass

    def change_loc(self):  # метод для входа и выхода из тоннеля
        if self.col < 0.5:
            self.col = 27.0

        if self.col > 27.0:
            self.col = 0.5

    def choose_direction_in_frightened(self):  # метод для выбора направления в испуге
        if self.dir == 0:
            self.random_choose_direction([0, 1, 3])

        elif self.dir == 1:
            self.random_choose_direction([0, 1, 2])

        elif self.dir == 2:
            self.random_choose_direction([1, 2, 3])

        elif self.dir == 3:
            self.random_choose_direction([0, 2, 3])

    def turn_in_impasse(self, moved):  # если призрак застрял, что бывает часто,
        # то он выбирает направление из возможных
        if not moved:
            if self.can_move_dir_up():
                self.dir = 0
            elif self.can_move_dir_right():
                self.dir = 1
            elif self.can_move_dir_bottom():
                self.dir = 2
            elif self.can_move_dir_left():
                self.dir = 3

    def random_choose_direction(self, directions):  # функция для случайного выбора направлений
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

    def can_move_in_this_dir(self, direction):  # функция, которая просматривает,
        # может ли призрак двигаться в каком-то направлении
        if direction == 0:
            if self.can_move_dir_up():
                return True
        elif direction == 1:
            if self.can_move_dir_right():
                return True
        elif direction == 2:
            if self.can_move_dir_bottom():
                return True
        elif direction == 3:
            if self.can_move_dir_left():
                return True

        return False

    def move(self):  # метод для самого передвижения призрака
        moved = False
        if self.dir == 0:
            if self.can_move_dir_up():
                self.row -= self.speed
                moved = True
        elif self.dir == 1:
            if self.can_move_dir_right():
                self.col += self.speed
                moved = True
        elif self.dir == 2:
            if self.can_move_dir_bottom():
                self.row += self.speed
                moved = True
        elif self.dir == 3:
            if self.can_move_dir_left():
                self.col -= self.speed
                moved = True

        self.turn_in_impasse(moved)  # проверка, не застрял ли призрак

        return moved

    def change_active(self):  # метод изменения активности, различный для каждого призрака
        pass

    def leave_home(self):  # метод выхода из дома призраков, различный для всех
        pass

    def can_move_dir_up(self):  # метод определения может ли призрак двигаться вверх
        if can_move(math.floor(self.row - self.speed), self.col, self.key_leave_home) \
                and self.col % 1.0 == 0 \
                and 2 != self.dir:
            return True
        return False

    def can_move_dir_right(self):  # метод определения может ли призрак двигаться вправо
        if can_move(self.row, math.ceil(self.col + self.speed), self.key_leave_home) \
                and self.row % 1.0 == 0 \
                and 3 != self.dir:
            return True
        return False

    def can_move_dir_bottom(self):  # метод определения может ли призрак двигаться вниз
        if can_move(math.ceil(self.row + self.speed), self.col, self.key_leave_home) \
                and self.col % 1.0 == 0 \
                and 0 != self.dir:
            return True
        return False

    def can_move_dir_left(self):  # метод определения может ли призрак двигаться влево
        if can_move(self.row, math.floor(self.col - self.speed), self.key_leave_home) \
                and self.row % 1.0 == 0 \
                and self.dir != 1:
            return True
        return False


class Blinky(Ghost):  # красный призрак, преследует Пакмана
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

    def change_direction(self):  # Блинки движется просто за Пакманом,
        # когда есть возможность где-то повернуть в сторону Пакмана, то он это делает
        if not self.active_frightened:
            if not self.active_scatter:
                vector = (self.col - game.pacman.col, self.row - game.pacman.row)

            else:
                vector = [self.col - 26.0, self.row - 6.0]

            dir_pacman_hor, dir_pacman_ver = find_direction(vector)

            if self.dir % 2 == 0:
                if dir_pacman_hor == 'r':
                    if self.can_move_dir_right():
                        self.dir = 1
                elif dir_pacman_hor == 'l':
                    if self.can_move_dir_left():
                        self.dir = 3
            else:
                if dir_pacman_ver == 'b':
                    if self.can_move_dir_bottom():
                        self.dir = 2
                elif dir_pacman_ver == 't':
                    if self.can_move_dir_up():
                        self.dir = 0

        else:
            self.choose_direction_in_frightened()


class Pinky(Ghost):  # розовый призрак, пытается обогнать Пакмана
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

    def change_active(self):  # выходит сразу же за Блинки
        self.active = True

    def leave_home(self):
        self.dir = 0
        if self.col >= 13.5 and self.row <= 14.0:
            self.key_leave_home = False

    def change_direction(self):  # выбирает клетку на четыре перед Пакманом и движется в эту точку,
        # таким образом он пытается обогнать Пакмана
        if not self.active_frightened:
            if not self.key_leave_home:
                pacman_dir = game.pacman.dir
                vector = tuple()
                if not self.active_scatter:
                    if pacman_dir == 0:
                        vector = (self.col - game.pacman.col, self.row - game.pacman.row + 4)
                    elif pacman_dir == 1:
                        vector = (self.col - game.pacman.col + 4, self.row - game.pacman.row)
                    elif pacman_dir == 2:
                        vector = (self.col - game.pacman.col, self.row - game.pacman.row - 4)
                    elif pacman_dir == 3:
                        vector = (self.col - game.pacman.col - 4, self.row - game.pacman.row)

                else:
                    vector = (self.col - 4.0, self.row - 6.0)

                dir_hor, dir_ver = find_direction(vector)

                if game.ghosts[0].row == self.row:
                    if self.can_move_dir_right():
                        self.dir = 1
                        return
                    elif self.can_move_dir_left():
                        self.dir = 3
                        return
                elif game.ghosts[0].col == self.col:
                    if self.can_move_dir_up():
                        self.dir = 0
                        return
                    elif self.can_move_dir_bottom():
                        self.dir = 2
                        return

                if self.dir % 2 != 0:
                    if dir_ver == 't':
                        if self.can_move_dir_up():
                            self.dir = 0
                            return
                    elif dir_ver == 'b':
                        if self.can_move_dir_bottom():
                            self.dir = 2
                            return
                else:
                    if dir_hor == 'l':
                        if self.can_move_dir_left():
                            self.dir = 3
                            return
                    elif dir_hor == 'r':
                        if self.can_move_dir_right():
                            self.dir = 1
                            return
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


class Inky(Ghost):  # бирюзовый призрак, обладает более сложным алгоритмом,
    # чем другие, сам алгоритм описан в функции change_direction
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

    def change_active(self):  # выходит, когда Пакман съест 30 точек
        if game.get_points() >= 30:
            self.active = True

    def leave_home(self):
        if self.row >= 14.0:
            self.dir = 0
        else:
            self.dir = 1
        if self.col >= 13.5 and self.row <= 14.0:
            self.key_leave_home = False

    def change_direction(self):  # выбирает точку на две перед Пакманом,
        # строит вектор от Блинки до этой точки,
        # удлинняет его вдвое и движется в получившуюся координату
        if not self.active_frightened:
            if not self.key_leave_home:
                if not self.active_scatter:
                    vector = [game.pacman.col,
                              game.pacman.row]
                    pacman_dir = game.pacman.dir
                    if pacman_dir == 0:
                        vector[1] += 2.0
                    elif pacman_dir == 1:
                        vector[0] += 2.0
                    elif pacman_dir == 2:
                        vector[1] -= 2.0
                    elif pacman_dir == 3:
                        vector[0] -= 2.0

                    vector = [(vector[0]) * 2 - game.ghosts[0].col,
                              (vector[1]) * 2 - game.ghosts[0].row]

                    vector = [self.col - vector[0], self.row - vector[1]]

                else:
                    vector = [self.col - 7.0, self.row - 30.0]

                dir_hor, dir_ver = find_direction(vector)

                if self.dir % 2 == 0:
                    if dir_hor == 'r':
                        if self.can_move_dir_right():
                            self.dir = 1
                    elif dir_hor == 'l':
                        if self.can_move_dir_left():
                            self.dir = 3
                else:
                    if dir_ver == 'b':
                        if self.can_move_dir_bottom():
                            self.dir = 2
                    elif dir_ver == 't':
                        if self.can_move_dir_up():
                            self.dir = 0
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


class Clyde(Ghost):  # оранжевый призрак, движется всегда случайно
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

    def change_active(self):  # выходит после того, как Пакман соберет 80 точек
        if game.get_points() >= 80:
            self.active = True

    def leave_home(self):
        if self.col >= 13.5:
            self.dir = 3
        else:
            self.dir = 0

        if self.col == 13.5 and self.row == 14.0:
            self.key_leave_home = False

    def change_direction(self):  # движется случайно в любой момент времени
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
                    vector = [self.col - 19.0, self.row - 30.0]

                    dir_hor, dir_ver = find_direction(vector)

                    if self.dir % 2 == 0:
                        if dir_hor == 'r':
                            if self.can_move_dir_right():
                                self.dir = 1
                        elif dir_hor == 'l':
                            if self.can_move_dir_left():
                                self.dir = 3
                    else:
                        if dir_ver == 'b':
                            if self.can_move_dir_bottom():
                                self.dir = 2
                        elif dir_ver == 't':
                            if self.can_move_dir_up():
                                self.dir = 0
            else:
                self.leave_home()
        else:
            self.choose_direction_in_frightened()


# инициализация игры и заставки
game = Game(1)
splash_screen()

# основной цикл игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # старт игры
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.started()
            play_music("game_start.wav")
        # изменение направление движений игрока
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.pacman.change_direction(0)
            elif event.key == pygame.K_d:
                game.pacman.change_direction(1)
            elif event.key == pygame.K_s:
                game.pacman.change_direction(2)
            elif event.key == pygame.K_a:
                game.pacman.change_direction(3)
    # если игры не остановления, то рисуем поле и обновляем картинку игры
    if not game.is_paused():
        game.render()
        game.update()
    # начала новой игры, если флаг истенен
    if new_game:
        game = Game()
        screen.fill((0, 0, 0))
        splash_screen()
        new_game = False
        game_board = copy.deepcopy(original_game_Board)
    pygame.display.flip()
    clock.tick(fps)
