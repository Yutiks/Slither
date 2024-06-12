import pygame as pg
from settings import *


class Snack:
    def __init__(self, x, y):
        self.rect = pg.Rect([x, y], [CELL_SIZE, CELL_SIZE])

    def render(self, display):
        pg.draw.rect(display, RED, self.rect)
