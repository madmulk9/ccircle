# Your solution goes in this file!

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
'''

class Solution:
    def __init__(self):
        self.moveCount = 0
        self.availablePaths = 0
        self.curDir = 'N'
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
                    self.availablePaths += 1
                cat.turnRight()
        return self.availablePaths

    # Choose your level here: 'easy', 'medium', or 'hard'!
    def getLevel(self):
        return 'easy'

    # Smaller pause time = faster simulation
    def getPauseTime(self):
        return 0.5

    # Your solution!
    def moveTowardPizza(self, cat):
        # Wheeeee!
        self.scan(cat)
        '''
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
        '''
        #if self.getLevel() == 'medium':
            #pass
        #self.moveCount += 1