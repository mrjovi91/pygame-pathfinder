from libs.colors import *

class MapView:
    def __init__(self, game, title, width, height, rows, columns, run_button_coordinates):
        self._game = game
        self._title = title
        self._width, self._height = width, height
        self._window = self._game.display.set_mode((self._width, self._height+100))
        self._game.display.set_caption(self._title)
        self._rows = rows
        self._columns = columns
        self._cell_width = width / columns
        self._cell_height = height / rows
        self._run_button_coordinates = run_button_coordinates
        
    def refresh(self, phase, grid):
        self._window.fill(WHITE)
        for y, row in enumerate(grid):
            for x, column in enumerate(row):
                cell = column
                if cell.start:
                    self._game.draw.rect(self._window, GREEN, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.end:
                    self._game.draw.rect(self._window, RED, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.disabled:
                    self._game.draw.rect(self._window, BLACK, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                else:
                    self._game.draw.rect(self._window, BLACK, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height), 1)
        if phase == 'Drawing':
            self._game.draw.rect(self._window, GREEN, self._game.Rect(self._run_button_coordinates[0], self._run_button_coordinates[1], self._run_button_coordinates[2], self._run_button_coordinates[3]))
            self._game.draw.rect(self._window, BLACK, self._game.Rect(self._run_button_coordinates[0], self._run_button_coordinates[1], self._run_button_coordinates[2], self._run_button_coordinates[3]), 1)
            font = self._game.font.Font(self._game.font.get_default_font(), 36)
            text_surface = font.render('Start', True, WHITE)
            self._window.blit(text_surface, dest=(self._run_button_coordinates[0] + self._run_button_coordinates[2]/3.5, self._run_button_coordinates[1]))

        self._game.display.update()