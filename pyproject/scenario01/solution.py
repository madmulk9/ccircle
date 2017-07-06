
import worlds
# Your solution goes in this file!
#taking that L

'''
    GOAL: Fill in the code for 'moveTowardPizza' to ensure that the cat finds the pizza!

    Use the following functions to understand the cat's situation:

        cat.isBlocked() -> Bool
            returns True if the cat is facing a wall or the edge of the maze, False if the coast is clear
        cat.isFacingN() -> Bool
            True iff cat is facing north
        cat.isFacingS() -> Bool
            True iff cat is facing south
        cat.isFacingE() -> Bool
            True iff cat is facing east
        cat.isFacingW() -> Bool
            True iff cat is facing west
        cat.smellsPizza() -> Bool
            True iff the cat is right in front of the pizza (and is facing it)

        Just a refresher...:

                   /|\
                    |
                  North
                    |
        <-- West --- --- East --->
                    |
                    |
                  South
                    |
                   \|/

    Use the following functions to instruct the cat:

        cat.turnLeft() -> None
            Instructs the cat to turn left / counter-clockwise
        cat.turnRight() -> None
            Instructs the cat to turn right / clockwise
        cat.walk() -> None
            Instructs the cat to walk in the direction it is facing

    NOTE: You can only call cat.walk() ONCE per call to moveTowardPizza!!
'''

class Solution:
    def __init__(self):
        self.moveCount = 0
        #                      N  E  S  W
        self.availablePaths = [0, 0, 0, 0]
        self.prevDir = ''
        pass

    def scan(self, cat):
        if not cat.isFacingN():
            #adjust north
            while not cat.isFacingN():
                cat.turnRight();
        elif cat.isFacingN():
            #the scan
            for n in range(3):
                if not cat.isBlocked():
                    self.availablePaths[n] = 1
                cat.turnRight()
        return self.availablePaths

    def move(self, cat):
        if self.availablePaths[0] == 1 and not self.prevDir == 'N':
            while not cat.isFacingN():
                cat.turnRight()
            while not cat.isBlocked():
                cat.walk()
        elif self.availablePaths[1] == 1 and not self.prevDir == 'E':
            while not cat.isFacingE():
                cat.turnRight()
            while not cat.isBlocked():
                cat.walk()
        elif self.availablePaths[2] == 1 and not self.prevDir == 'S':
            while not cat.isFacingS():
                cat.turnRight()
            while not cat.isBlocked():
                cat.walk()
        elif self.availablePaths[3] == 1 and not self.prevDir == 'W':
            while not cat.isFacingW():
                cat.turnRight()
            while not cat.isBlocked():
                cat.walk()


    # Choose your level here: 'easy', 'medium', or 'hard'!
    def getLevel(self):
        return worlds.easy()

    # Smaller pause time = faster simulation
    def getPauseTime(self):
        return 0.5

    # Your solution!
    def moveTowardPizza(self, cat):
        # Wheeeee!
        self.scan(cat)
        self.move(cat)
        print(self.scan(cat))
        """
        if self.getLevel() == 'easy':
            if self.moveCount < 2:
                cat.turnRight()
            elif self.moveCount < 3:
                cat.walk()
            elif self.moveCount < 4:
                cat.turnRight()
            elif self.moveCount < 7:
                cat.walk()
            elif self.moveCount < 8:
                cat.turnLeft()
            elif self.moveCount < 10:
                cat.walk()
            elif self.moveCount < 11:
                cat.turnLeft()
            elif self.moveCount < 12:
                cat.walk()
            elif self.moveCount < 13:
                cat.turnRight()
            elif self.moveCount < 15:
                cat.walk()
            elif self.moveCount < 16:
                cat.turnRight()
            elif self.moveCount < 19:
                cat.walk()
            elif self.moveCount < 20:
                cat.turnRight()
            elif self.moveCount < 21:
                cat.walk()
        """
        #if self.getLevel() == 'medium':
            #pass
        #self.moveCount += 1