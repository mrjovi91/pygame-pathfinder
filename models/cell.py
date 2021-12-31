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

    def click(self):
        if self.disabled:
            self.disabled = False
            self.start = True
            self.end = False
        elif self.start:
            self.disabled = False
            self.start = False
            self.end = True
        elif self.end:
            self.disabled = False
            self.start = False
            self.end = False
        else:
            self.disabled = True
            self.start = False
            self.end = False