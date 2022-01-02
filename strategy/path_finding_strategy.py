from abc import ABC, abstractmethod

class PathFindingStrategy(ABC):
    def __init__(self, grid):
        self._grid = grid

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def render_completed(self):
        pass

    @abstractmethod
    def display_path(self):
        pass

    @abstractmethod
    def display_path_completed(self):
        pass