import ccircle

window = ccircle.Window()
window.toggleMaximized()
winX, winY = window.getSize()
r = 0.0
g = 0.0
b = 0.0
size = 8
hasUpped = False

points = []

while window.isOpen():
    window.clear(1, 1, 1)
    mx, my = window.getMousePos()

    if ccircle.isKeyDown('up'):
        if not hasUpped:
            size += 2
            hasUpped = True
    elif ccircle.isKeyDown('down'):
        if not hasUpped:
            size -= 2
            hasUpped = True
    else:
        if hasUpped:
            hasUpped = False



    if ccircle.isMouseDown('left'):
        if (mx >= 10 and mx <= 50) and (my >= 10 and my <= 50):
            r = 0.0
            g = 0.0
            b = 0.0
        elif (mx >= 10 and mx <= 50) and (my >= 60 and my <= 100):
            r = 1.0
            g = 0.0
            b = 0.0
        elif (mx >= 10 and mx <= 50) and (my >= 110 and my <= 150):
            r = 0.0
            g = 1.0
            b = 0.0
        elif (mx >= 10 and mx <= 50) and (my >= 160 and my <= 200):
            r = 0.0
            g = 0.0
            b = 1.0
        else:
            window.hideMouse()
            points.append((mx, my, size, r, g, b))
    else:
        window.showMouse()

    window.drawCircle(mx, my, size, r, g, b)
    for x, y, ssize, sr, sg, sb in points:
        window.drawCircle(x, y, ssize, sr, sg, sb)
    window.drawRect(0, 0, 50, winY)
    window.drawRect(10, 10, 40, 40, 0, 0, 0)
    window.drawRect(10, 60, 40, 40, 1, 0, 0)
    window.drawRect(10, 110, 40, 40, 0, 1, 0)
    window.drawRect(10, 160, 40, 40, 0, 0, 1)
    window.update()