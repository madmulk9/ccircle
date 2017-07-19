import ccircle

class Character:
    def __init__(self, isPlayer, x=400, y=400, maxHP = 100, maxStam = 25):
        self.x = x
        self.y = y
        if isPlayer:
            self.isPlayer = True
            self.spriteSheet = ccircle.Image("pctransframes.png")
            self.frames = {
                "idle": [(12, 12, 28, 66),
                         (47, 12, 28, 66)],
                "dodgeLeft": [(12, 84, 26, 64),
                              (46, 84, 26, 64),
                              (78, 84, 26, 64)],
                "dodgeRight": ['''cannot be implemented until image flip'''],
                "damaged": [],
                "attack": [(11, 308, 32, 85),
                           (45, 308, 32, 85),
                           (77, 308, 32, 85)],
                "blocked": [],
                "ko": []
            }
        else:
            self.isPlayer = False
            self.frames = {
                "idle": [],
                "dodgeLeft": [],
                "dodgeRight": [],
                "damaged": [],
                "attack": [],
                "blocked": [],
                "ko": []
            }
        self.isBlocking = False
        self.isDodging = {
            "left": False,
            "right": False
        }
        self.maxStamina = maxStam
        self.stamina = self.maxStamina
        self.maxHP = maxHP
        self.hp = self.maxHP
        self.isTired = False
        self.regcd = 0.3
        self.tiredcd = 1.0
        self.cd = self.regcd

    def dodge(self, dodgeDir):
        if dodgeDir == "l":
            self.isDodging["left"] = True
            self.isDodging["right"] = False
        if dodgeDir == "r":
            self.isDodging["right"] = True
            self.isDodging["left"] = False

    def punch(self, enemyBlock):
        if not self.isPlayer:
            pass
        else:
            if enemyBlock:
                if self.stamina >= 1:
                    self.stamina -= 1
                    return 0
                else:
                    return 0
            else:
                return 10 # abstract damage number to the enemy

    def getBlock(self):
        return self.isBlocking

    def setBlock(self, isBlocking):
        if isBlocking: self.isBlocking = True
        else: self.isBlocking = False

    def takeDamage(self, damage):
        if damage >= self.hp:
            self.hp = 0
        else:
            self.hp -= int(damage)

    def p_animLoop(self, state, count):
        if self.isTired:
            self.cd = self.tiredcd
        else:
            self.cd = self.regcd
        if state == "idle":
            self.isDodging["left"] = False
            self.isDodging["right"] = False
            if count < .45:
                self.spriteSheet.drawSub(self.x - 2, self.y, 28*1.25, 66*1.25, *self.frames["idle"][0])
            else:
                self.spriteSheet.drawSub(self.x + 2, self.y, 28*1.25, 66*1.25, *self.frames["idle"][1])
        elif state == "punch":
            self.isDodging["left"] = False
            self.isDodging["right"] = False
            if count < self.cd * 0.16666666666:
                self.spriteSheet.drawSub(self.x, self.y + 5, 28 * 1.25, 66 * 1.25, *self.frames["attack"][0])
            elif count < self.cd * 0.33333333333:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28 * 1.25, 66 * 1.25, *self.frames["attack"][1])
            elif count < self.cd * 0.83333333333:
                self.spriteSheet.drawSub(self.x, self.y - 30, 28 * 1.25, 66 * 1.25, *self.frames["attack"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28 * 1.25, 66 * 1.25, *self.frames["attack"][1])
        elif state == "dodgeLeft":
            if count < self.cd * 0.13333333333:
                self.spriteSheet.drawSub(self.x - 3, self.y, 28 * 1.25, 66 * 1.25, *self.frames["dodgeLeft"][0])
            elif count < self.cd * 0.26666666666:
                self.spriteSheet.drawSub(self.x - 15, self.y, 28 * 1.25, 66 * 1.25, *self.frames["dodgeLeft"][1])
            elif count < self.cd * 0.86666666666:
                self.spriteSheet.drawSub(self.x - 20, self.y, 28 * 1.25, 66 * 1.25, *self.frames["dodgeLeft"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x - 15, self.y, 28 * 1.25, 66 * 1.25, *self.frames["dodgeLeft"][1])
        elif state == "dodgeRight":
            pass
