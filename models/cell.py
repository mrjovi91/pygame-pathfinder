class Cell:
    def __init__(self, x, y, head=False, start=False, end=False, disabled=False):
        self._x = x
        self._y = y
        self.start = start
        self.end = end
        self.disabled = disabled
        self.state = None
        
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def click(self, start_is_set, end_is_set):
        old_state = self.state
        if start_is_set and end_is_set:
            if self.disabled:
                self.state = 'end'
                self.disabled = False
                self.start = False
                self.end = True
        else:
            if end_is_set:
                if self.start:
                    self.state = 'end'
                    self.disabled = False
                    self.start = False
                    self.end = True

            if start_is_set:
                if self.disabled:
                    self.state = 'start'
                    self.disabled = False
                    self.start = True
                    self.end = False


        if self.disabled:
            self.state = 'start'
            self.disabled = False
            self.start = True
            self.end = False
        elif self.start:
            self.state = 'end'
            self.disabled = False
            self.start = False
            self.end = True
        elif self.end:
            self.state = None
            self.disabled = False
            self.start = False
            self.end = False
        else:
            self.state = 'disabled'
            self.disabled = True
            self.start = False
            self.end = False
        return old_state, self.state