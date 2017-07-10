import ccircle
import cloud
import house
import world
import random

window = ccircle.Window('Lab', 800, 600)
myWorld = world.World()

for i in range(100):
    x = random.randint(0,800)
    y = random. randint (0, 150)
    size = random.randint (25, 100)
    myWorld.add(cloud.Cloud(x, y, size))

for i in range(4):
    x = random.randint(5, 755)
    baseColor = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
    myWorld.add(house.House(x, baseColor))

while window.isOpen():
    window.clear(1, 1, 1)
    myWorld.draw(window)
    myWorld.update()
    window.update()