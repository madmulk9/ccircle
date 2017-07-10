import random
class House:
    def __init__(self, x, baseColor, roofColor=[0.3, 0.3, 0.3]):
        self.x = x
        self.y = 360
        self.sy = self.y
        self.baseColor = baseColor
        self.roofColor = roofColor
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(0, 10)
        self.my = random.randint(1, 10)

    def draw(self, window):
        window.drawRect(self.x, self.y, 40, 40, *self.baseColor)
        window.drawTri(self.x - 5, self.y, self.x + 20, self.y - 20, self.x + 45, self.y, *self.roofColor)
        self.drawSmoke(window, 20)

    def drawSmoke(self, window, count):
        for i in range(count):
            window.drawCircle(self.x + self.vx, self.sy - self.vy, 10, .6, .6, .6, .25)
            print("made a smoke")

    def update(self, dt):
        self.sy -= self.my * dt
        if self.sy < self.y - 40:
            self.sy = self.y
