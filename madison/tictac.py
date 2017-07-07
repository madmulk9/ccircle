import ccircle

window = ccircle.Window("issa tic tac too", 324, 346)

class Square:
    def __init__(self, vPos, hPos):
        self.claimed = False
        self.size = 100
        self.colors = [0.0, 0.0, 0.0]
        self.vPos = 0
        self.hPos = 0
        self.drawHitbox(vPos, hPos)
        print("initialized at " + hPos + ", " + vPos)

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
        if not self.claimed:
            self.colors = [0.0, 0.0, 0.0]
        else:
            self.colors = [1.0, 1.0, 1.0]
        window.drawRect(self.hPos, self.vPos, self.size, self.size, *self.colors)

    def onClick(self, mX, mY):
        if ccircle.isMouseDown('left') and ((mX >= self.hPos and mX <= self.hPos + self.size)
                                            and (mY >= self.vPos and mY <= self.vPos + self.size)):
            self.claimed = True
        elif ccircle.isMouseDown('right') and ((mX >= self.hPos and mX <= self.hPos + self.size)
                                            and (mY >= self.vPos and mY <= self.vPos + self.size)):
            self.claimed = False

squares = [Square('t', 'l'), Square('t', 'c'), Square('t', 'r'),
           Square('m', 'l'), Square('m', 'c'), Square('m', 'r'),
           Square('b', 'l'), Square('b', 'c'), Square('b', 'r')]



while window.isOpen():
    window.clear(1, 1, 1)
    mouseX, mouseY = window.getMousePos()
    for i in range(len(squares)):
        squares[i].onClick(mouseX, mouseY)
        squares[i].updateHitbox()

    window.drawLine(0, 102, 308, 102, 4, .2, .2, .2)
    window.drawLine(0, 206, 308, 206, 4, .2, .2, .2)
    window.drawLine(102, 0, 102, 308, 4, .2, .2, .2)
    window.drawLine(206, 0, 206, 308, 4, .2, .2, .2)
    # detect clicks on square object
    # update with the cross or circle

    window.update()