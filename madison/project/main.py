import ccircle
import character
import time

window = ccircle.Window("Punch-Out!", 1024, 1024)
background = ccircle.Image("bg.png")
bgcolor = [0.364705882, 0.58039215686, 0.98431372549]
gameblack = [0, 0.01176470588, 0.01176470588]
textFont = ccircle.Font("pofont.ttf")
textColor = [0.69019607843, 0.95294117647, 0.73333333333]
textShadow = [0.803921568627451, 0.22745098039215686, 0.1568627450980392]
pc = character.Character(True)
enemy = character.Character(False)
hpcolor = [1.0, 0.988235294, 1.0]
keyDown = False
dt = 1.0 / 60.0
frameCount = time.perf_counter()
x = 50
cd = 0.5
count = 0
idlecount = 0
curloop = ""

def renderBG():
    # background stuff
    window.clear(0, 0, 0)
    background.draw(0, 0, 1024, 1024)
    # clearing visible logos and pre-existing numbers
    window.drawRect(825, 62, 135, 74, *bgcolor)
    window.drawRect(425, 100, 350, 36, *bgcolor)
    window.drawRect(116, 64, 44, 48, *gameblack)
    window.drawRect(216, 64, 72, 48, *gameblack)

    # hp tracker and draw
    window.drawRect(352, 68, 192, 28, *gameblack)
    window.drawRect(352, 68, 192 * (enemy.hp / enemy.maxHP), 28, *hpcolor)
    # counter spaces
      # star counter (cur. unused)
    textFont.draw("0", 132, 100, 16, *textShadow)
    textFont.draw("0", 128, 100, 16, *textColor)
      # stam counter
    if pc.stamina < 10:
        textFont.draw("0" + str(pc.stamina), 228, 100, 16, *textShadow)
        textFont.draw("0" + str(pc.stamina), 224, 100, 16, *textColor)
    else:
        textFont.draw(str(pc.stamina), 228, 100, 16, *textShadow)
        textFont.draw(str(pc.stamina), 224, 100, 16, *textColor)

while window.isOpen():
    renderBG()

    # trackers based on dt (no visualization)
    idlecount += dt
    cd += dt

    # control area
    if ccircle.isKeyDown("up"):
        if not keyDown:
            if cd > .5:
                enemy.takeDamage(pc.punch(False))
                keyDown = True
                cd = 0
                curloop = "punch"
    elif ccircle.isKeyDown("left"):
        if not keyDown:
            if cd > .5:
                pc.dodge("l")
                keyDown = True
                cd = 0
    elif ccircle.isKeyDown("right"):
        if not keyDown:
            if cd > .5:
                pc.dodge("r")
                keyDown = True
                cd = 0
    else:
        keyDown = False
        curloop = "idle"
        pc.animLoop(curloop, idlecount)

    if cd < .5:
        count += dt
        pc.animLoop(curloop, count)

    window.update()

    #animation frame tracker reset
    if idlecount > .9:
        idlecount = 0
    if count > .5:
        count = 0

    #time updater
    newCount = time.perf_counter()
    dt = newCount - frameCount
    frameCount = newCount