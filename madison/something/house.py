class House:
    def __init__(self, x, baseColor, roofColor=[0.3, 0.3, 0.3]):
        self.x = x
        self.baseColor = baseColor
        self.roofColor = roofColor

    def draw(self, window):
        window.drawRect(self.x, 360, 40, 40, *self.baseColor)
        window.drawTri(self.x - 5, 360, self.x + 20, 340, self.x + 45, 360, *self.roofColor)

    def update(self):
        pass