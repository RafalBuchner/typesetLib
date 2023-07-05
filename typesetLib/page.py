from typesetLib.basic import BasicLayoutGraphicObject


class Page(BasicLayoutGraphicObject):
    def __init__(self, size, index=0, startPgNumber=1):
        super().__init__(size, index)
        self.setStartingPgNumber(startPgNumber)

    @property
    def currentPgNumber(self):
        return self.startPgNumber + self.index

    def pageFlip(self):
        """
        means, that page has changed by 1
        """
        self.index += 1

    def resetPgNumberToStart(self):
        self.setCurrentPgNumber(self.startPgNumber)

    def setStartingPgNumber(self, pgNumber):
        self.startPgNumber = pgNumber

    def setCurrentPgNumber(self, pgNumber):
        self.index = pgNumber - self.startPgNumber

    def setIndex(self, value):
        self.index = value

    # not supported inherented methods:
    def setParent(self, obj):
        NotImplemented

    def setPosition(self, obj):
        NotImplemented

    def getPosition(self, obj):
        NotImplemented
