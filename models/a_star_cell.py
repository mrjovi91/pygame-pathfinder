from models.cell import Cell

class AStarCell:
    def __init__(self, cell):
        self._cell = cell
        self.start = False
        self.end = False
        self._g = float('inf') # Distance from starting node
        self._h = float('inf') # Distance from end node
        self._f = float('inf') # G cost + H cost

    def set_cost(self, g, h):
        self._g = g
        self._h = h
        self._f = g + h

    @property
    def cell(self):
        return self._cell

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @property
    def f(self):
        return self._f

    @property
    def row(self):
        return self._cell.y
    
    @property
    def column(self):
        return self._cell.x