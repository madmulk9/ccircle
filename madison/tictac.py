import ccircle

window = ccircle.Window("issa tic tac too", 324, 346)

class Square:
    def __init__(self, vPos, hPos):
        self.claimed = False
        self.xClaimed = False
        self.oClaimed = False
        self.size = 100
        self.colors = [1.0, 1.0, 1.0]
        self.initVPos = vPos
        self.vPos = 0
        self.initHPos = hPos
        self.hPos = 0
        self.drawHitbox(vPos, hPos)
        print("initialized at " + self.initHPos + ", " + self.initVPos)

    def drawHitbox(self, vPos, hPos):
        if vPos == 't':
            if hPos == 'l':
                window.drawRect(0, 0, self.size, self.size, *self.colors)
                self.vPos = 0
                self.hPos = 0
            elif hPos == 'c':
                window.drawRect(104, 0, self.size, self.size, *self.colors)
                self.vPos = 0
                self.hPos = 104
            elif hPos == 'r':
                window.drawRect(208, 0, self.size, self.size, *self.colors)
                self.vPos = 0
                self.hPos = 208
            else:
                raise Exception("No horizontal position defined when instantiating class Square.")
        elif vPos == 'm':
            if hPos == 'l':
                window.drawRect(0, 104, self.size, self.size, *self.colors)
                self.vPos = 104
                self.hPos = 0
            elif hPos == 'c':
                window.drawRect(104, 104, self.size, self.size, *self.colors)
                self.vPos = 104
                self.hPos = 104
            elif hPos == 'r':
                window.drawRect(208, 104, self.size, self.size, *self.colors)
                self.vPos = 104
                self.hPos = 208
            else:
                raise Exception("No horizontal position defined when instantiating class Square.")
        elif vPos == 'b':
            if hPos == 'l':
                window.drawRect(0, 208, self.size, self.size, *self.colors)
                self.vPos = 208
                self.hPos = 0
            elif hPos == 'c':
                window.drawRect(104, 208, self.size, self.size, *self.colors)
                self.vPos = 208
                self.hPos = 104
            elif hPos == 'r':
                window.drawRect(208, 208, self.size, self.size, *self.colors)
                self.vPos = 208
                self.hPos = 208
            else:
                raise Exception("No horizontal position defined when instantiating class Square.")
        else:
            raise Exception("No vertical position defined when instantiating class Square.")

    def updateHitbox(self):
        window.drawRect(self.hPos, self.vPos, self.size, self.size, *self.colors)
        if self.xClaimed:
            window.drawLine(self.hPos + 10, self.vPos + 10, self.hPos + 90, self.vPos + 90, 4, 0, 0, 0)
            window.drawLine(self.hPos + 10, self.vPos + 90, self.hPos + 90, self.vPos + 10, 4, 0, 0, 0)
        if self.oClaimed:
            window.drawCircle(self.hPos + 50, self.vPos + 50, 45, 0, 0, 0)
            window.drawCircle(self.hPos + 50, self.vPos + 50, 41, 1, 1, 1)

    def onClick(self, mX, mY):
        if ccircle.isMouseDown('left') and ((mX >= self.hPos and mX <= self.hPos + self.size)
                                            and (mY >= self.vPos and mY <= self.vPos + self.size)):
            if not self.claimed:
                self.xClaimed = True
                self.claimed = True
        elif ccircle.isMouseDown('right') and ((mX >= self.hPos and mX <= self.hPos + self.size)
                                            and (mY >= self.vPos and mY <= self.vPos + self.size)):
            if not self.claimed:
                self.oClaimed = True
                self.claimed = True

    def reset(self):
        self.claimed = False
        self.xClaimed = False
        self.oClaimed = False

squares = [Square('t', 'l'), Square('t', 'c'), Square('t', 'r'),
           Square('m', 'l'), Square('m', 'c'), Square('m', 'r'),
           Square('b', 'l'), Square('b', 'c'), Square('b', 'r')]



while window.isOpen():
    window.clear(1, 1, 1)

    mouseX, mouseY = window.getMousePos()

    if ccircle.isKeyDown('r'):
        for i in range(len(squares)):
            squares[i].reset()
    for i in range(len(squares)):
        squares[i].onClick(mouseX, mouseY)
        squares[i].updateHitbox()

    window.drawLine(0, 102, 308, 102, 4, .2, .2, .2)
    window.drawLine(0, 206, 308, 206, 4, .2, .2, .2)
    window.drawLine(102, 0, 102, 308, 4, .2, .2, .2)
    window.drawLine(206, 0, 206, 308, 4, .2, .2, .2)

    window.update()