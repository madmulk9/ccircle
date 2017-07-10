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
for i in range(20):
    myBall.append(ball.Ball(random.randint(200, 600), random.randint(100, 400)))
    myWorld.add(myBall[i])


start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(1, 1, 1)
    for i in range(len(myBall)):
        myBall[i].applyForce(0, 1000)

    myWorld.draw(window)
    myWorld.update(dt * 3)
    window.update()

    now = time.time()
    dt = now - start
    start = now
