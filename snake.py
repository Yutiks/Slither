from settings import *


class Snake:
    def __init__(self):
        self.parts_of_snake = [pg.Rect([0, 0], [CELL_SIZE, CELL_SIZE])]
        self.rect = self.parts_of_snake[0].unionall(self.parts_of_snake)

    def render(self, display):
        for part in self.parts_of_snake:
            pg.draw.rect(display, BLACK, part)

    def grow(self):
        new_part = pg.Rect(self.parts_of_snake[-1].x, self.parts_of_snake[-1].y, CELL_SIZE, CELL_SIZE)
        self.parts_of_snake.append(new_part)

    def movement(self, direction):
        for move_each in range(len(self.parts_of_snake) - 1, 0, -1):
            self.parts_of_snake[move_each].x = self.parts_of_snake[move_each - 1].x
            self.parts_of_snake[move_each].y = self.parts_of_snake[move_each - 1].y
        if direction == "right":
            self.parts_of_snake[0].x += CELL_SIZE + 1
        elif direction == "left":
            self.parts_of_snake[0].x -= CELL_SIZE + 1
        elif direction == "down":
            self.parts_of_snake[0].y += CELL_SIZE + 1
        elif direction == "up":
            self.parts_of_snake[0].y -= CELL_SIZE + 1
        self.rect = self.parts_of_snake[0].unionall(self.parts_of_snake)
