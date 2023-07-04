from typesetLib.abstract.basic import GraphicBasicObject


class LayoutTextBox(GraphicBasicObject):
	"""
	- story (Story)
	"""
	NotImplemented

	def assignToStory(self, story):
		self.story = story
		idx = len(self.story.textBoxes) - 1
		self.setIndex(idx)

	@property
	def nextTextBox(self):
		if self.story is None:
			return None

		nextIndex = self.index + 1
		if nextIndex >= len(self.story.textBoxes):
			return None

		return self.story.textBoxes[nextIndex]

	@property
	def prevTextBox(self):
		if self.story is None:
			return None

		prevIndex = self.index - 1
		if prevIndex < 0:
			return None

		return self.story.textBoxes[prevIndex]



