import pygame as pg
from settings import *


class Cell:
    def __init__(self, cell_x, cell_y):
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.rect = pg.Rect([self.cell_x, self.cell_y], [CELL_SIZE, CELL_SIZE])
        self.colour = GREEN

    def render(self, display):
        pg.draw.rect(display, self.colour, (self.cell_x, self.cell_y, CELL_SIZE, CELL_SIZE))
