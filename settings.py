import pygame.freetype
import pygame as pg
pg.init()

# DISPLAY PARAMETERS -->
WIDTH = 800
HEIGHT = 800

# COLOURS -->
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# NUMBER OF CELLS ALONG THE 'X' AND 'Y' AXES
CELL_NUMBER_X = 16
CELL_NUMBER_Y = int(HEIGHT / (WIDTH / CELL_NUMBER_X))
CELL_SIZE = WIDTH / CELL_NUMBER_X - 1

# FPS LIMIT -->
FPS = 60

FONT = pygame.freetype.Font("fonts/main_font_2.ttf", 50)
