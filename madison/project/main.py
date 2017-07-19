import ccircle
import character
import time

window = ccircle.Window("Punch-Out!", 1024, 1024)
background = ccircle.Image("bg.png")
colors = {
    "bgcolor": [0.364705882, 0.58039215686, 0.98431372549],
    "gameblack": [0, 0.01176470588, 0.01176470588],
    "textColor": [0.69019607843, 0.95294117647, 0.73333333333],
    "textShadow": [0.803921568627451, 0.22745098039215686, 0.1568627450980392],
    "hpcolor": [1.0, 0.988235294, 1.0]
}
textFont = ccircle.Font("pofont.ttf")
pc = character.Character(True)
enemy = character.Character(False)
dt = 1.0 / 60.0
frameCount = time.perf_counter()
cdtime = 0.3
cd = cdtime
count = 0
idlecount = 0
curloop = ""
hasDamaged = False
toggle = False

def renderBG():
    # background stuff
    window.clear(0, 0, 0)
    background.draw(0, 0, 1024, 1024)
    # clearing visible logos and pre-existing numbers
    window.drawRect(825, 62, 135, 74, *colors["bgcolor"])
    window.drawRect(425, 100, 350, 36, *colors["bgcolor"])
    window.drawRect(116, 64, 44, 48, *colors["gameblack"])
    window.drawRect(216, 64, 72, 48, *colors["gameblack"])

    # hp tracker and draw
      # player's
    window.drawRect(352, 68, 192, 28, *colors["gameblack"])
    window.drawRect(352, 68, 192 * (pc.hp / pc.maxHP), 28, *colors["hpcolor"])
      # enemy's
    window.drawRect(768, 68, -192, 28, *colors["gameblack"])
    window.drawRect(768, 68, -192 * (enemy.hp / enemy.maxHP), 28, *colors["hpcolor"])
    # counter spaces
      # star counter (cur. unused)
    textFont.draw("0", 132, 100, 16, *colors["textShadow"])
    textFont.draw("0", 128, 100, 16, *colors["textColor"])
      # stam counter
    if pc.stamina < 10:
        textFont.draw("0" + str(pc.stamina), 228, 100, 16, *colors["textShadow"])
        textFont.draw("0" + str(pc.stamina), 224, 100, 16, *colors["textColor"])
    else:
        textFont.draw(str(pc.stamina), 228, 100, 16, *colors["textShadow"])
        textFont.draw(str(pc.stamina), 224, 100, 16, *colors["textColor"])

while window.isOpen():
    renderBG()

    if ccircle.wasKeyPressed('b') and not toggle:
        enemy.setBlock(True)
        toggle = True
    elif ccircle.wasKeyPressed('b') and toggle:
        enemy.setBlock(False)
        toggle = False

    # trackers based on dt (no visualization)
    idlecount += dt
    cd += dt

    if pc.isTired:
        cdtime = 1.0
    else:
        cdtime = 0.3

    # control area
    if cd < cdtime:
        count += dt
        if cd > cdtime / 3 and curloop == "punch" and not hasDamaged:
            enemy.takeDamage(pc.punch(enemy.getBlock()))
            hasDamaged = True
        pc.p_animLoop(curloop, count)
    elif ccircle.wasKeyPressed("up"):
        if cd > cdtime:
            hasDamaged = False
            cd = 0
            count = 0
            curloop = "punch"
    elif ccircle.wasKeyPressed("left"):
        if cd > cdtime:
            pc.dodge("l")
            cd = 0
            count = 0
            curloop = "dodgeLeft"
    elif ccircle.wasKeyPressed("right"):
        if cd > cdtime:
            pc.dodge("r")
            keyDown = True
            cd = 0
            count = 0
            curloop = "dodgeRight"
    elif ccircle.wasKeyPressed("down"):
        pc.takeDamage(enemy.punch(pc.getBlock()))
    else:
        keyDown = False
        curloop = "idle"
        pc.p_animLoop(curloop, idlecount)

    # TODO: Add accurate sizes of icons

    # TODO: Round timer

    # TODO: Win condition

    window.update()

    # idle animation frame tracker reset
    if idlecount > .9:
        idlecount = 0

    # time updater
    newCount = time.perf_counter()
    dt = newCount - frameCount
    frameCount = newCount