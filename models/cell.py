class Cell:
    def __init__(self, x, y, head=False, start=False, end=False, disabled=False):
        self._x = x
        self._y = y
        self.start = start
        self.end = end
        self.disabled = disabled
        

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y