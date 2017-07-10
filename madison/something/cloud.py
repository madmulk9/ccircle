class Cloud:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, window):
        window.drawCircle(self.x, self.y, self.size, 1, 1, 1, 0.25)

    def update(self):
        pass