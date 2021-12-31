from settings import settings
from views.map_view import MapView
from models.cell import Cell

import pygame
from pygame.locals import *
from time import sleep
import random

class MapController:

    def __init__(self):
        self._game = pygame
        self._run = True
        self._start = False
        self._clock = self._game.time.Clock()
        
        self.rows = 15
        self.columns = 15
        self._grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.columns):
                row.append(Cell(x, y))
            self._grid.append(row)

        # self._snake = [[int(self.rows/2), int(self.columns/2)]]
        # self._grid[self._snake[0][0]][self._snake[0][1]].head = True
        # self._direction = 'right'
        # self._sleep = 0.25

        # self.determine_new_food()

        self._display = MapView(self._game, "Path Finder", 600, 600, self.rows, self.columns)

    # def determine_new_food(self):
    #     while True:
    #         new_food = random.choice(random.choice(self._grid))
    #         if not new_food.body and not new_food.head and not (new_food.x <= 0 or new_food.y <= 0 or new_food.x >= self.columns -1 or new_food.y >= self.rows - 1):
    #             new_food.food = True
    #             break

    def run(self):
        while self._run:
            self._display.refresh(self._grid)
            self._clock.tick(settings['fps'])
            # if len(self._snake) % 5 == 0:
            #     if self._sleep <= 0.05:
            #         self._sleep = 0.05
            #     else:
            #         self._sleep /= 1.01
            # sleep(self._sleep)
            for event in self._game.event.get():
                if event.type == self._game.QUIT:
                    self._run = False
                elif event.type == self._game.MOUSEBUTTONUP:
                    pos = self._game.mouse.get_pos()
                    x = int(pos[0] / self._display._cell_width)
                    y = int(pos[1] / self._display._cell_height)
                    self._grid[y][x].click()



            # keys_pressed = self._game.key.get_pressed()
            # if keys_pressed[self._game.K_w] and self._direction is not 'down':
            #     self._direction = 'up'
            # elif keys_pressed[self._game.K_d] and self._direction is not 'left':
            #     self._direction = 'right'
            # elif keys_pressed[self._game.K_s] and self._direction is not 'up':
            #     self._direction = 'down'
            # elif keys_pressed[self._game.K_a] and self._direction is not 'right':
            #     self._direction = 'left'

            # if not self.move():
            #     break
        self._game.quit()

    # def move(self):
    #     directions = {
    #         'up': [-1, 0],
    #         'right': [0, 1],
    #         'down': [1, 0],
    #         'left': [0, -1]
    #     }

    #     new_head_coordinates = [self._snake[0][0] + directions[self._direction][0], self._snake[0][1] + directions[self._direction][1]]
    #     new_head = self._grid[new_head_coordinates[0]][new_head_coordinates[1]]

    #     if new_head_coordinates[0] < 0 or new_head_coordinates[1] >= self.rows or new_head_coordinates[1] < 0 or new_head_coordinates[1] >= self.columns or new_head.body:
    #         return False

    #     current_head = self._grid[self._snake[0][0]][self._snake[0][1]]
    #     current_head.head = False
    #     current_head.body = True
    #     new_head.head = True
    #     new_head.body = False
    #     self._snake.insert(0, new_head_coordinates)

    #     if current_head.food:
    #         current_head.food = False
    #         self.determine_new_food()
    #     else:
    #         current_tail = self._grid[self._snake[-1][0]][self._snake[-1][1]]
    #         new_tail = self._grid[self._snake[-2][0]][self._snake[-2][1]]
    #         current_tail.body = False
    #         new_tail.body = True
    #         self._snake.remove(self._snake[-1])
    #     return True

            
        