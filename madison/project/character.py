import ccircle

class Character:

    '''
    IN PUNCHOUT:
    - Dodging
    - Blocking (enemy)
    - Punching
      - Punching a block
    - Stamina
      - Getting Tired
    '''

    def __init__(self, isPlayer, x=400, y=400, maxHP = 100, maxStam = 25):
        self.x = x
        self.y = y
        if isPlayer:
            self.isPlayer = True
            self.spriteSheet = ccircle.Image("pctransframes.png")
            self.frames = {
                "idle": [(12, 12, 28, 66),
                         (47, 12, 28, 66)],
                "dodgeLeft": [],
                "dodgeRight": [],
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
        self.isIdle = True

    def dodge(self, dodgeDir, dodgeLen = 1.5):
        if dodgeDir == "l":
            self.isDodging["left"] = True
            self.isDodging["right"] = False
        if dodgeDir == "r":
            self.isDodging["right"] = True
            self.isDodging["left"] = False

    def punch(self, enemyBlock, strikeDir=None):
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

    def setBlock(self, isBlocking):
        if isBlocking: self.isBlocking = True
        else: self.isBlocking = False

    def takeDamage(self, damage):
        if damage >= self.hp:
            self.hp = 0
        else:
            self.hp -= int(damage)

    def animLoop(self, state, count):
        if state == "idle":
            if count < .45:
                self.spriteSheet.drawSub(self.x - 2, self.y, 28*1.25, 66*1.25, *self.frames["idle"][0])
            else:
                self.spriteSheet.drawSub(self.x + 2, self.y, 28*1.25, 66*1.25, *self.frames["idle"][1])
        elif state == "punch":
            if count < .05:
                self.spriteSheet.drawSub(self.x, self.y + 5, 28*1.25, 66*1.25, *self.frames["attack"][0])
            elif count < .10:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28*1.25, 66*1.25, *self.frames["attack"][1])
            elif count < .25:
                self.spriteSheet.drawSub(self.x, self.y - 30, 28*1.25, 66*1.25, *self.frames["attack"][2])
            elif count < .3:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28*1.25, 66*1.25, *self.frames["attack"][1])
        elif state == "dodgeLeft":
            pass
        elif state == "dodgeRight":
            pass
