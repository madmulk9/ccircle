import ccircle
import cloud
import ball
import house
import world
import random
import time

window = ccircle.Window('Lab', 800, 600)
myWorld = world.World()

for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = random.randint(25, 100)
    myWorld.add(cloud.Cloud(x, y, size))

'''
for i in range(4):
    x = random.randint(5, 755)
    baseColor = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
    myWorld.add(house.House(x, baseColor))
'''
myBall = []
for i in range(1000):
    myBall.append(ball.Ball(random.randint(50, 750), random.randint(50, 450)))
    myWorld.add(myBall[i])


start = time.time()
dt = 1.0 / 60.0

def bounce(inc):
    for i in range(len(myBall)):
        myBall[i].applyForce(0, -inc)

while window.isOpen():
    window.clear(1, 1, 1)
    mouseX, mouseY = window.getMousePos()
    if ccircle.isKeyDown('space'):
        bounce(300)
    else:
        for i in range(len(myBall)):
            myBall[i].applyForce(0, 1000)

    for i in range(len(myBall)):
        if ((myBall[i].x - mouseX) ** 2) == 0 or ((myBall[i].y - mouseY) ** 2) == 0:
            myBall[i].applyForce((myBall[i].x - mouseX) / ((myBall[i].x - mouseX + 1) ** 2) * 3500,
                                 (myBall[i].y - mouseY) / ((myBall[i].y - mouseY + 1) ** 2) * 3500)
        else:
            myBall[i].applyForce((myBall[i].x - mouseX) / ((myBall[i].x - mouseX) ** 2) * 3500,
                                 (myBall[i].y - mouseY) / ((myBall[i].y - mouseY) ** 2) * 3500)

    myWorld.draw(window)
    myWorld.update(dt)
    window.update()

    now = time.time()
    dt = now - start
    start = now
