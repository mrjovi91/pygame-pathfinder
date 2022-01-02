from models.cell import Cell
from models.dijkstra_cell import DijkstraCell
from strategy.path_finding_strategy import PathFindingStrategy

from queue import PriorityQueue
import random

class DijkstraPathFindingStrategy(PathFindingStrategy):
    DISTANCE_BETWEEN_CELLS = 10
    def __init__(self, grid, start, end):

        self._open_set = PriorityQueue()
        self._current = None
        self._from_list = {}
        self._rows = len(grid)
        self._columns = len(grid[0])
        
        formatted_grid = []
        for i, row in enumerate(grid):
            formatted_grid.append([])
            for j, cell in enumerate(row):
                formatted_grid[i].append(DijkstraCell(cell))

        self._start = formatted_grid[start[1]][start[0]]
        self._end = formatted_grid[end[1]][end[0]]

        self._end.end = True
        self._start.cell.current = True
        self._start.cost = 0
        self._start.start = True

        self._count = 0
        self._open_set.put((self._start.cost, self._count , self._start))
        self._closed_set = [self._start]
        super().__init__(formatted_grid)

    # def heuristic(self, cell):
    #     dx = abs(cell.column - self._end.column)
    #     dy = abs(cell.row - self._end.row)
    #     return DijkstraPathFindingStrategy.DISTANCE_BETWEEN_CELLS * (dx + dy)


    def get_visitable_neighbours(self):
        neighbours = []
        row = self._current.row
        column = self._current.column

        directions = {
            'up': [-1, 0],
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1]
        }

        for coordinates in directions.values():
            try:
                y = coordinates[0] + row
                x = coordinates[1] + column
                if y < 0 or y >= self._rows or x < 0 or x >= self._columns:
                    continue

                attempted_cell = self._grid[y][x]
                if attempted_cell.cell.disabled:
                    continue


                if attempted_cell.cell.neighbour:
                    attempted_cell.cell.computed = True
                attempted_cell.cell.neighbour = True
                neighbours.append(attempted_cell)
                
            except:
                continue

        return neighbours

    def render(self):
        neighbours = self.get_visitable_neighbours()
        for neighbour in neighbours:
            temp_cost = self._current.cost + DijkstraPathFindingStrategy.DISTANCE_BETWEEN_CELLS
            if temp_cost < neighbour.cost:
                self._from_list[neighbour] = self._current
                neighbour.cost = temp_cost

                if neighbour not in self._closed_set:
                    self._count += 1
                    self._open_set.put((neighbour.cost, self._count, neighbour))
                    self._closed_set.append(neighbour)

    def render_completed(self):
        if self._open_set.empty():
            return True
        
        if not self._current == None:
            self._current.cell.current = False

        self._current = self._open_set.get()[2]
        self._current.cell.current = True
        self._closed_set.remove(self._current)

        if self._current == self._end:
            self._current.cell.current = False
            return True
        return False

    def display_path(self):
        self._current.cell.path = True
        self._current = self._from_list[self._current]

    def display_path_completed(self):
        if self._current == self._start:
            self._current.cell.path = True
            return True
        return False

    def __str__(self):
        return 'Dijkstra Path Finding Algorithm'