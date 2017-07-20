import ccircle

class Character:
    def __init__(self, isMainPlayer, x=400, y=400, maxHP = 150, maxStam = 15):
        self.initX = x
        self.x = x
        self.initY = y
        self.y = y
        if isMainPlayer:
            self.isMainPlayer = True
            self.spriteSheet = ccircle.Image("pctransframes.png")
            self.frames = {
                "idle": [(12, 12, 28, 66),
                         (47, 12, 28, 66)],
                "dodgeLeft": [(12, 84, 26, 64),
                              (46, 84, 26, 64),
                              (78, 84, 26, 64)],
                "dodgeRight": [(12, 84, 26, 64),
                               (160, 83, 26, 64),
                               (193, 83, 26, 64)],
                "damaged": [(12, 566, 30, 64),
                            (50, 566, 28, 64)],
                "attack": [(11, 308, 32, 85),
                           (45, 308, 32, 85),
                           (77, 308, 32, 85)],
                "ko": [(12, 566, 30, 64),
                       (50, 566, 28, 64),
                       (91, 566, 32, 64)]
            }
        else:
            self.isMainPlayer = False
            self.spriteSheet = ccircle.Image("medtrans.png")
            self.frames = {
                "idle": [(8, 250, 45, 113),
                         (65, 250, 45, 113),
                         (123, 250, 47, 113)],
                "damaged": [(8, 498, 54, 111),
                            (74, 498, 57, 111)],
                "attack": [(8, 619, 55, 112),
                           (142, 619, 55, 112),
                           (192, 619, 55, 112)],
                "ko": [(8, 1112, 62, 106),
                       (80, 1110, 53, 108),
                       (146, 1110, 61, 108)]
            }
        self.isDamaged = False
        self.isDodging = False
        self.maxStamina = maxStam
        self.stamina = self.maxStamina
        self.maxHP = maxHP
        self.hp = self.maxHP
        self.isTired = False
        self.regcd = 0.3
        self.tiredcd = 1.0
        self.cd = self.regcd

    def dodge(self, isDodging):
        if isDodging: self.isDodging = True
        else: self.isDodging = False

    def getDodge(self):
        return self.isDodging

    def punch(self, isDodging):
        if not isDodging:
            if self.stamina == 0:
                self.stamina += 5
            return 10
        else:
            if self.stamina > 0:
                self.stamina -= 1
            return 0

    def getKO(self):
        if self.hp == 0: return True
        else: return False

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
            self.isDodging = False
            if count < .45:
                self.spriteSheet.drawSub(self.x - 2, self.y, 28 * 2.25, 66 * 2.25, *self.frames["idle"][0])
            else:
                self.spriteSheet.drawSub(self.x + 2, self.y, 28 * 2.25, 66 * 2.25, *self.frames["idle"][1])
        elif state == "punch":
            self.isDodging = False
            if count < self.cd * 0.16666666666:
                self.spriteSheet.drawSub(self.x, self.y + 2, 28 * 2.25, 66 * 2.25, *self.frames["attack"][0])
            elif count < self.cd * 0.33333333333:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28 * 2.25, 66 * 2.25, *self.frames["attack"][1])
            elif count < self.cd * 0.83333333333:
                self.spriteSheet.drawSub(self.x, self.y - 30, 28 * 2.25, 66 * 2.25, *self.frames["attack"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x, self.y - 15, 28 * 2.25, 66 * 2.25, *self.frames["attack"][1])
        elif state == "dodgeLeft":
            if count < self.cd * 0.13333333333:
                self.spriteSheet.drawSub(self.x - 3, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeLeft"][0])
            elif count < self.cd * 0.26666666666:
                self.spriteSheet.drawSub(self.x - 15, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeLeft"][1])
            elif count < self.cd * 0.86666666666:
                self.spriteSheet.drawSub(self.x - 20, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeLeft"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x - 15, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeLeft"][1])
        elif state == "dodgeRight":
            if count < self.cd * 0.13333333333:
                self.spriteSheet.drawSub(self.x + 3, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeRight"][0])
            elif count < self.cd * 0.26666666666:
                self.spriteSheet.drawSub(self.x + 15, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeRight"][1])
            elif count < self.cd * 0.86666666666:
                self.spriteSheet.drawSub(self.x + 20, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeRight"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x + 15, self.y, 28 * 2.25, 66 * 2.25, *self.frames["dodgeRight"][1])
        elif state == "damaged":
            if count < .05:
                self.spriteSheet.drawSub(self.x + 2, self.y, 28 * 2.25, 66 * 2.25, *self.frames["damaged"][0])
            elif count < .35:
                self.spriteSheet.drawSub(self.x + 10, self.y, 28 * 2.25, 66 * 2.25, *self.frames["damaged"][1])
        elif state == "ko":
            if count < 1.0:
                self.spriteSheet.drawSub(self.x, self.y, 28 * 2.25, 66 * 2.25, *self.frames["ko"][0])
            elif count < 2.0:
                self.spriteSheet.drawSub(self.x, self.y, 28 * 2.25, 66 * 2.25, *self.frames["ko"][1])
            else:
                self.spriteSheet.drawSub(self.x, self.y, 28 * 2.25, 66 * 2.25, *self.frames["ko"][2])

    def e_animLoop(self, state, count):
        if self.isTired:
            self.cd = self.tiredcd
        else:
            self.cd = self.regcd
        if state == "idle":
            self.isDodging = False
            # other player has more idle frames
            if count < .225:
                self.spriteSheet.drawSub(self.x - 2, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][0])
            elif count < .45:
                self.spriteSheet.drawSub(self.x, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
            elif count < .675:
                self.spriteSheet.drawSub(self.x + 2, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][2])
            else:
                self.spriteSheet.drawSub(self.x, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
        elif state == "dodgeLeft":
            if count < self.cd * 0.13333333333:
                self.spriteSheet.drawSub(self.x - 5, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
            elif count < self.cd * .26666666666:
                self.spriteSheet.drawSub(self.x - 25, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][0])
            elif count < self.cd * 0.86666666666:
                self.spriteSheet.drawSub(self.x - 40, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][0])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x - 25, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
        elif state == "dodgeRight":
            if count < self.cd * 0.13333333333:
                self.spriteSheet.drawSub(self.x + 3, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
            elif count < self.cd * .26666666666:
                self.spriteSheet.drawSub(self.x + 25, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][2])
            elif count < self.cd * 0.86666666666:
                self.spriteSheet.drawSub(self.x + 40, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][2])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x + 25, self.y, 44 * 2.25, 84 * 2.25, *self.frames["idle"][1])
        elif state == "punch":
            self.isDodging = False
            if count < self.cd * 0.16666666666:
                self.spriteSheet.drawSub(self.x, self.y + 2, 44 * 2.25, 84 * 2.25, *self.frames["attack"][0])
            elif count < self.cd * 0.33333333333:
                self.spriteSheet.drawSub(self.x, self.y - 15, 44 * 2.25, 84 * 2.25, *self.frames["attack"][1])
            elif count < self.cd:
                self.spriteSheet.drawSub(self.x, self.y - 30, 44 * 2.25, 84 * 2.25, *self.frames["attack"][2])
        elif state == "damaged":
            if count < .05:
                self.spriteSheet.drawSub(self.x + 2, self.y, 44 * 2.25, 84 * 2.25, *self.frames["damaged"][0])
            elif count < .35:
                self.spriteSheet.drawSub(self.x + 10, self.y, 44 * 2.25, 84 * 2.25, *self.frames["damaged"][1])
        elif state == "ko":
            if count < 1.0:
                self.spriteSheet.drawSub(self.x, self.y, 44 * 2.25, 84 * 2.25, *self.frames["ko"][0])
            elif count < 2.0:
                self.spriteSheet.drawSub(self.x, self.y, 44 * 2.25, 84 * 2.25, *self.frames["ko"][1])
            else:
                self.spriteSheet.drawSub(self.x, self.y, 44 * 2.25, 84 * 2.25, *self.frames["ko"][2])

    def animLoop(self, state, count):
        if self.isMainPlayer:
            self.p_animLoop(state, count)
        else:
            self.e_animLoop(state, count)

    def reset(self):
        self.__init__(self.isMainPlayer, self.initX, self.initY, self.maxHP, self.maxStamina)
