import random
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0#random.randint(40, 100)
        self.vy = 0
        self.fx = 0
        self.fy = 0
        self.mass = 1

    def applyForce(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        window.drawCircle(self.x, self.y, 16, 0, 0, 0)
        window.drawCircle(self.x, self.y, 14, 1, 0, 0.2)

    def update(self, dt):
        accelX = self.fx / self.mass
        accelY = self.fy / self.mass
        self.vx += dt * accelX
        self.vy += dt * accelY
        self.x += dt * self.vx
        self.y += dt * self.vy
        self.fx = 0
        self.fy = 0

        if self.x < 0:
            self.vx *= -0.9
            self.x = 0

        if self.x > 800:
            self.vx *= -0.9
            self.x = 800

        if self.y > 500:
            self.vy *= -0.9
            self.y = 500

        if self.y < 0:
            self.vy *= -0.9
            self.y = 0