from settings import settings
from views.map_view import MapView
from models.cell import Cell
from strategy.a_star_path_finding import AStarPathFindingStrategy

import pygame
from pygame.locals import *
from time import sleep
import random

class MapController:

    def __init__(self):
        self._game = pygame
        self._run = True
        self._phase = 'Drawing'

        self._start = None
        self._end = None
        self._clock = self._game.time.Clock()
        
        self.rows = settings['rows']
        self.columns = settings['columns']
        self._cell_width = settings['width'] / self.columns
        self._cell_height = settings['height'] / self.rows
        self._run_button_coordinates = (self.columns/3 * self._cell_width, settings['height'] + settings['menu_height']/4, self._cell_width * self.columns/3, self._cell_height)

        self._grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.columns):
                row.append(Cell(x, y))
            self._grid.append(row)

        self._display = MapView(self._game, "Path Finder", settings['width'], settings['height'], self.rows, self.columns,self._run_button_coordinates)
        self._path_finding_strategy = None


    def run(self):
        while self._run:
            if self._path_finding_strategy is None:
                self._display.refresh(self._phase, self._grid)
            else:
                self._display.refresh(self._phase, self._path_finding_strategy._grid)
            self._clock.tick(settings['fps'])

            if self._phase == 'Drawing':
                for event in self._game.event.get():
                    if event.type == self._game.QUIT:
                        self._run = False
                    elif event.type == self._game.MOUSEBUTTONUP:
                        pos = self._game.mouse.get_pos()
                        if pos[1] > settings['height']:
                            if self._start and self._end and (pos[0] > self._run_button_coordinates[0]) and (pos[0] < self._run_button_coordinates[0] + self._run_button_coordinates[2]) and (pos[1] > self._run_button_coordinates[1]) and (pos[1] <  self._run_button_coordinates[1] + self._run_button_coordinates[3]):
                                self._phase = "Generate Path"
                                print(f'Start: {self._start}')
                                print(f'End: {self._end}')
                                self._path_finding_strategy = AStarPathFindingStrategy(self._grid, self._start, self._end)
                        else:
                            x = int(pos[0] / self._display._cell_width)
                            y = int(pos[1] / self._display._cell_height)
                            old_state, new_state = self._grid[y][x].click(self._start, self._end)
                            if old_state == 'start':
                                self._start = None
                            elif old_state == 'end':
                                self._end = None

                            if new_state == 'start':
                                self._start = [x,y]
                            elif new_state == 'end':
                                self._end = [x,y]

            elif self._phase == 'Generate Path':
                for event in self._game.event.get():
                    if event.type == self._game.QUIT:
                        self._run = False

                if self._path_finding_strategy.render_completed():
                    self._phase = 'Display Path'
                    continue

                self._path_finding_strategy.render()
                sleep(0.125)
                
                
            elif self._phase == 'Display Path':
                for event in self._game.event.get():
                    if event.type == self._game.QUIT:
                        self._run = False
                self._path_finding_strategy.display_path()
                self._display.refresh(self._phase, self._path_finding_strategy._grid)
                self._clock.tick(settings['fps'])

                if self._path_finding_strategy.display_path_completed():
                    self._phase = 'Completed'

            else:
                for event in self._game.event.get():
                    if event.type == self._game.QUIT:
                        self._run = False
                

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

            
        