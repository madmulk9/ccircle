import ccircle
import character
import controller
import time

window = ccircle.Window("Punch-Out!", 1024, 1024)
background = ccircle.Image("bg.png")
colors = {
    "bgcolor": [0.364705882, 0.58039215686, 0.98431372549],
    "gameblack": [0, 0.01176470588, 0.01176470588],
                # red,               blue,               green
    "textColor": [0.658823549747467, 0.7372549176216125, 0.9411764740943909],
    "textShadow": [0.803921568627451, 0.22745098039215686, 0.1568627450980392],
    "hpcolor": [1.0, 0.988235294, 1.0]
}
textFont = ccircle.Font("pofont.ttf")
pc = character.Character(True, 475, 600)
play2 = character.Character(False, 450, 500)
dt = 1.0 / 60.0
frameCount = time.perf_counter()
kocount = 0
mainPlayerController = controller.Controller(pc, play2, "w", "a", "d")
sidePlayerController = controller.Controller(play2, pc, "up", "left", "right")

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
      # player 1's
    window.drawRect(352, 68, 192, 28, *colors["gameblack"])
    window.drawRect(352, 68, 192 * (pc.hp / pc.maxHP), 28, *colors["hpcolor"])
      # player 2's
    window.drawRect(768, 68, -192, 28, *colors["gameblack"])
    window.drawRect(768, 68, -192 * (play2.hp / play2.maxHP), 28, *colors["hpcolor"])
    # counter spaces
      # star counter (also stam counter)
    if play2.stamina < 10:
        textFont.draw("0" + str(play2.stamina), 106, 100, 16, *colors["textShadow"])
        textFont.draw("0" + str(play2.stamina), 102, 100, 16, *colors["textColor"])
    else:
        textFont.draw(str(play2.stamina), 106, 100, 16, *colors["textShadow"])
        textFont.draw(str(play2.stamina), 102, 100, 16, *colors["textColor"])
      # stam counter
    if pc.stamina < 10:
        textFont.draw("0" + str(pc.stamina), 228, 100, 16, *colors["textShadow"])
        textFont.draw("0" + str(pc.stamina), 224, 100, 16, *colors["textColor"])
    else:
        textFont.draw(str(pc.stamina), 228, 100, 16, *colors["textShadow"])
        textFont.draw(str(pc.stamina), 224, 100, 16, *colors["textColor"])

while window.isOpen():
    renderBG()

    if pc.isTired:
        pccdtime = 1.0
    else:
        pccdtime = 0.3

    if play2.isTired:
        p2cdtime = 1.0
    else:
        p2cdtime = 0.3

    # control area
    if not pc.getKO() and not play2.getKO():
        sidePlayerController.controlLoop(dt, p2cdtime)
        mainPlayerController.controlLoop(dt, pccdtime)
    else:
        if pc.getKO() and not play2.getKO():
            # player 2 wins
            play2.e_animLoop("idle", sidePlayerController.idlecount)
            pc.p_animLoop("ko", kocount)
            kocount += dt
            if kocount < 2:
                pc.y += dt * 45
            elif kocount > 2 and kocount < 3:
                pc.y += dt * 100
            elif kocount > 3:
                textFont.drawCentered("PLAYER 2 WINS!", 518, 306, 24, *colors["textShadow"])
                textFont.drawCentered("PLAYER 2 WINS!", 512, 300, 24, *colors["textColor"])
                textFont.drawCentered("Press R to restart", 518, 406, 18, *colors["textShadow"])
                textFont.drawCentered("Press R to restart", 512, 400, 18, *colors["textColor"])
                if ccircle.isKeyDown("r"):
                    pc.reset()
                    play2.reset()
                    kocount = 0
        elif not pc.getKO() and play2.getKO():
            play2.e_animLoop("ko", kocount)
            pc.p_animLoop("idle", mainPlayerController.idlecount)
            kocount += dt
            if kocount < 1:
                play2.y -= dt * 40
            elif kocount > 1 and kocount < 2:
                play2.y -= dt * 100
            elif kocount > 2:
                textFont.drawCentered("PLAYER 1 WINS!", 518, 306, 24, *colors["textShadow"])
                textFont.drawCentered("PLAYER 1 WINS!", 512, 300, 24, *colors["textColor"])
                textFont.drawCentered("Press R to restart", 518, 406, 18, *colors["textShadow"])
                textFont.drawCentered("Press R to restart", 512, 400, 18, *colors["textColor"])
                if ccircle.isKeyDown("r"):
                    pc.reset()
                    play2.reset()
                    kocount = 0
        else:
            # double KO, nobody wins
            print("what")
            pass

    window.update()

    # time updater
    newCount = time.perf_counter()
    dt = newCount - frameCount
    frameCount = newCount