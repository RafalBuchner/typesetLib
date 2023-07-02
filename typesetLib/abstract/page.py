from typesetLib.abstract.basic import LayoutBasicObject


class AbstractPage(LayoutBasicObject):
	def __int__(self, index, startPgNumber=0):
		super().__int__(index)
		self.startPgNumber = startPgNumber

	@property
	def currentPgNumber(self):
		return self.startPgNumber + self.index