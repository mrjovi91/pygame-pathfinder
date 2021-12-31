from libs.colors import *

class MapView:
    def __init__(self, game, title, width, height, rows, columns):
        self._game = game
        self._title = title
        self._width, self._height = width, height
        self._window = self._game.display.set_mode((self._width, self._height+100))
        self._game.display.set_caption(self._title)
        self._rows = rows
        self._columns = columns
        self._cell_width = width / columns
        self._cell_height = height / rows
        
    def refresh(self, grid):
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
        self._game.display.update()