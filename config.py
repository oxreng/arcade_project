# Настройки экрана
import os.path
from os import listdir
from os.path import isfile, join

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1600, 900)
HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT = SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1
WINDOW_NAME = 'GAME'

# Цвета
ORANGE = 'Orange'
PURPLE = 'Purple'
BLACK = 'Black'
SKYBLUE = 'Skyblue'
DARKGREY = 'Darkgrey'
YELLOW = 'Yellow'
GREEN = 'Green'
RED = 'Red'
WHITE = 'White'
BRICK = (139, 79, 57)
ANTHRACITE = (45, 45, 45)
BLUE = 'Blue'
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
UI_TEXT_COLOR = '#EEEEEE'
UI_HEALTH_COLOR = RED
UI_BORDER_COLOR_ACTIVE = 'gold'

# Настройки меню
MENU_FPS = 30
MENU_FONT = 'fonts/font.ttf'
BUTTON_FONT_SIZE = 75
LOGO_FONT_SIZE = 250
MENU_BACKGROUND = 'StartWindow.jpg'
MENU_BACKGROUND_POS = (0, 0)
EXIT_NAME = 'EXIT'
START_NAME = 'START'
BTN_EXIT_BACK_POS = (50, 500)
BTN_EXIT_BACK_SIZE = (150, 60)
BTN_START_BACK_POS = (50, 100)
BTN_START_BACK_SIZE = (200, 60)

# Настройки текстур
TILE = 100
TEXTURES_PATH = 'TextureSprite'
PLAYER_PATH = 'TextureSprite/player'
PASSABLE_TEXTURES_PATH = 'TextureSprite/passable_textures'
SOLID_TEXTURES_PATH = 'TextureSprite/solid_textures'
PLAYER_TEXTURES_PATH = 'TextureSprite/player'
SPRITE_ANIMATION_SPEED = 25

# Настройки камеры
BOX_LEFT = 450
BOX_RIGHT = BOX_LEFT
BOX_TOP = 300
BOX_BOTTOM = BOX_TOP
BOX_LEFT_ZOOM = 150
BOX_LEFT_MIN = BOX_LEFT - 2 * BOX_LEFT_ZOOM
BOX_TOP_ZOOM = 100
BOX_TOP_MIN = BOX_TOP - 2 * BOX_TOP_ZOOM
BOX_RIGHT_ZOOM = BOX_LEFT_ZOOM
BOX_RIGHT_MIN = BOX_RIGHT - 2 * BOX_RIGHT_ZOOM
BOX_BOTTOM_ZOOM = BOX_TOP_ZOOM
BOX_BOTTOM_MIN = BOX_BOTTOM - 2 * BOX_BOTTOM_ZOOM
MIN_ZOOM = 0.9
MAX_ZOOM = 0.7

# Настройки игрока
FPS = 60
PLAYER_SPEED = 8
PLAYER_ANIMATION_SPEED = 0.1
PLAYER_ATTACK_COOLDOWN = 400
PLAYER_INTERACTION_COOLDOWN = 500
PLAYER_STAT_HP = 100
PLAYER_STAT_ATTACK = 60

# UI
UI_BAR_HEIGHT = 20
UI_HEALTH_BAR_WIDTH = 200
UI_HEALTH_BAR_COORDS = (10, 10)
UI_FONT = 'fonts/joystix.ttf'
UI_FONT_SIZE = 18

# Настройки врагов
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'slash', 'speed': 3,
              'resistance': 3, 'attack_radius': 80, 'notice_radius': 360}
}

# Настройки анимаций
TELLY_FRAMES_COUNT = 2

# Музыка
MENU_THEME = 'music/menu.mp3'
MUSIC_FOLDER = 'Levels_music'
MUSIC_FILES = [os.path.join(MUSIC_FOLDER, file) for file in listdir(MUSIC_FOLDER) if isfile(join(MUSIC_FOLDER, file))]

# Подсказки
hint_text = {
    'door': 'Press  E  to  open',
    'oven': 'Press  E  to  interact',
    'wardrobe': 'Press  E  to  get  changed'
}
