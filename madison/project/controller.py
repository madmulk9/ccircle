import ccircle
import character
import time

class Controller:
    def __init__(self, character, enemy, keyATK, keyDGL, keyDGR):
        self.char = character
        self.enemy = enemy
        self.hasDamaged = False
        self.cd = 0
        self.count = 0
        self.idlecount = 0
        self.dmgcount = 0
        self.curloop = ""
        self.keyATK = keyATK
        self.keyDGL = keyDGL
        self.keyDGR = keyDGR

    def controlLoop(self, dt, cdtime):
        # trackers based on dt (no visualization)
        self.idlecount += dt
        self.cd += dt

        if self.cd < cdtime:
            self.count += dt
            if self.cd > cdtime / 3 and self.cd < (2 * cdtime) / 3 and self.curloop == "punch" and not self.hasDamaged:
                self.dmgcount = 0
                prevHP = self.enemy.hp
                self.enemy.takeDamage(self.char.punch(self.enemy.getDodge()))
                self.hasDamaged = True
                if prevHP > self.enemy.hp:
                    self.enemy.isDamaged = True
            self.char.animLoop(self.curloop, self.count)
        elif ccircle.wasKeyPressed(self.keyATK):
            if self.cd > cdtime:
                self.hasDamaged = False
                self.char.dodge(False)
                self.cd = 0
                self.count = 0
                self.curloop = "punch"
        elif ccircle.wasKeyPressed(self.keyDGL):
            if self.cd > cdtime:
                self.char.dodge(True)
                self.cd = 0
                self.count = 0
                self.curloop = "dodgeLeft"
        elif ccircle.wasKeyPressed(self.keyDGR):
            if self.cd > cdtime:
                self.char.dodge(True)
                self.cd = 0
                self.count = 0
                self.curloop = "dodgeRight"
        else:
            if self.char.getDodge() and self.cd >= cdtime:
                self.char.dodge(False)

            if self.char.isDamaged:
                self.char.animLoop("damaged", self.dmgcount)
                self.dmgcount += dt
                if self.dmgcount >= .35:
                    self.char.isDamaged = False
                    self.curloop = "idle"
                    self.dmgcount = 0
            else:
                self.curloop = "idle"
                self.char.animLoop(self.curloop, self.idlecount)

        if self.char.stamina == 0:
            self.char.isTired = True
        else:
            self.char.isTired = False

        # idle animation frame tracker reset
        if self.idlecount > .9:
            self.idlecount = 0