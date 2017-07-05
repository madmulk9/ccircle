import ccircle

window = ccircle.Window("work dang flabbit")
y = 124
eyebrows = True
while window.isOpen():
    window.clear(0, 0, 0)
    window.drawCircle(256, 192, 128, .8, .8, 0)
    window.drawCircle(192, 148, 24, 1, 1, 1)
    window.drawCircle(192, 148, 12, 0, 0, 0)
    window.drawCircle(320, 148, 24, 1, 1, 1)
    window.drawCircle(320, 148, 12, 0, 0, 0)
    window.drawRect(168, 124, 176, 8, .8, .8, 0)
    window.drawLine(127, 220, 384, 220, 20, 0, 0, 0)
    window.drawLine(127, 225, 384, 225, 20, 0, 0, 0)
    window.drawLine(168, y, 216, y, 20, .4, .2, .2)
    window.drawLine(296, y, 344, y, 20, .4, .2, .2)
    window.update()
    if eyebrows:
        y -= .2
        if y <= 100:
            eyebrows = False
    else:
        y += .2
        if y >= 124:
            eyebrows = True