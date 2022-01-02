from models.cell import Cell

class DijkstraCell:
    def __init__(self, cell):
        self._cell = cell
        self.start = False
        self.end = False
        self.cost = float('inf') # Distance from starting node

    @property
    def cell(self):
        return self._cell

    @property
    def row(self):
        return self._cell.y
    
    @property
    def column(self):
        return self._cell.x