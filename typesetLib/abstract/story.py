from typesetLib.abstract.basic import ProofBasicObject


class Story(ProofBasicObject):
	def __init__(self, textObj):
		self.textObj = textObj
		self.textBoxes = []


	def addTextBox(self, layoutTextBox):
		self.textBoxes.assignToStory(self)





