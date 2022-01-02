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
        self._game.init()
        self._font =  self._game.font.Font(self._game.font.get_default_font(), 36)

    def _render_run_button(self):
        self._game.draw.rect(self._window, GREEN, self._game.Rect(self._run_button_coordinates[0], self._run_button_coordinates[1], self._run_button_coordinates[2], self._run_button_coordinates[3]))
        self._game.draw.rect(self._window, BLACK, self._game.Rect(self._run_button_coordinates[0], self._run_button_coordinates[1], self._run_button_coordinates[2], self._run_button_coordinates[3]), 1)
        
        text_surface = self._font.render('Start', True, WHITE)
        self._window.blit(text_surface, dest=(self._run_button_coordinates[0] + self._run_button_coordinates[2]/3.5, self._run_button_coordinates[1]))

    def _render_cells(self, phase, grid):
        for y, row in enumerate(grid):
            for x, column in enumerate(row):
                if phase == 'Drawing':
                    cell = column
                else:
                    cell = column.cell

                if cell.start:
                    self._game.draw.rect(self._window, GREEN, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.end:
                    self._game.draw.rect(self._window, PURPLE, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.disabled:
                    self._game.draw.rect(self._window, BLACK, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.path:
                    self._game.draw.rect(self._window, ORANGE, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.computed:
                    self._game.draw.rect(self._window, BLUE, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))
                elif cell.neighbour:
                    self._game.draw.rect(self._window, RED, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height))

                self._game.draw.rect(self._window, BLACK, self._game.Rect(x*self._cell_width, y*self._cell_height, self._cell_width, self._cell_height), 1)
                
        
    def refresh(self, phase, grid):
        self._window.fill(WHITE)
        self._render_cells(phase, grid)
        if phase == 'Drawing':
            self._render_run_button()

        self._game.display.update()
