import pygame as pg
from settings import *
import cell
import snake
import snack_for_snake as snack
import random

pg.init()


class Game:
    def __init__(self):
        # GAME DATA -->
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        # CELL DATA -->
        self.cell_x = 0
        self.cell_y = 0
        self.x_axis_cells = 0
        self.cells = self.create_cells()

        # SNAKE DATA -->
        self.snake = snake.Snake()
        self.direction_snake = "right"
        self.speed_snake = pg.USEREVENT
        pg.time.set_timer(self.speed_snake, 100)
        length_at_beginning = 3
        for i in range(length_at_beginning):
            self.length_begin = self.snake.grow()

        # SNACK DATA -->
        self.random_place_x = []
        self.random_place_y = []
        self.each_cell_distance_x = 0
        self.each_cell_distance_y = 0
        for snack_ in range(CELL_NUMBER_X):
            self.random_place_x.append(self.each_cell_distance_x)
            self.each_cell_distance_x += (CELL_SIZE + 1)
        for snack_ in range(CELL_NUMBER_Y):
            self.random_place_y.append(self.each_cell_distance_y)
            self.each_cell_distance_y += (CELL_SIZE + 1)
        self.snack = snack.Snack(random.choice(self.random_place_x), random.choice(self.random_place_y))

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d and self.direction_snake != "left":
                    self.direction_snake = "right"
                elif event.key == pg.K_a and self.direction_snake != "right":
                    self.direction_snake = "left"
                elif event.key == pg.K_s and self.direction_snake != "up":
                    self.direction_snake = "down"
                elif event.key == pg.K_w and self.direction_snake != "down":
                    self.direction_snake = "up"
            if event.type == self.speed_snake:
                self.snake.movement(self.direction_snake)

    def create_cells(self):
        cells = []
        for i in range(CELL_NUMBER_X * CELL_NUMBER_Y + CELL_NUMBER_Y - 1):
            if self.x_axis_cells < CELL_NUMBER_X:
                new_cell = cell.Cell(self.cell_x, self.cell_y)
                cells.append(new_cell)
                self.cell_x += CELL_SIZE + 1
                self.x_axis_cells += 1
            elif self.x_axis_cells >= CELL_NUMBER_X:
                self.cell_y += CELL_SIZE + 1
                self.cell_x = 0
                self.x_axis_cells = 0
        return cells

    def render(self):
        self.display.fill(WHITE)
        for cell_from_list in self.cells:
            cell_from_list.render(self.display)
        self.snake.render(self.display)
        self.snack.render(self.display)
        pg.display.flip()

    def movement(self):
        if self.snake.rect.right > WIDTH or self.snake.rect.left < 0:
            self.running = False
        if self.snake.rect.bottom > HEIGHT or self.snake.rect.top < 0:
            self.running = False
        if self.snake.rect.colliderect(self.snack.rect):
            self.snack.rect.x = random.choice(self.random_place_x)
            self.snack.rect.y = random.choice(self.random_place_y)
            self.snake.grow()

    def run(self):
        while self.running:
            self.render()
            self.events()
            self.movement()
        self.clock.tick(FPS)


game = Game()
game.run()
