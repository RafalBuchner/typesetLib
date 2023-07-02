class ProofBasicObject(object):
	def __init__(self):
		self.userData = {}

	def setUserData(self, key, data):
		self.userData[key] = data

	def getUserData(self, key):
		return self.userData[key]

class TextFlowBasicObject(ProofBasicObject):
	def __init__(self, index):
		self.index = index

	def indexUP(self):
		self.index += 1

	def indexDOWN(self):
		NotImplemented

class GraphicBasicObject(TextFlowBasicObject):
	def __init__(self, index, size, position=None):
		super().__init__(index)
		self.setSize(size)
		if position is not None:
			self.setPosition(position)

	def setSize(self, size):
		self.width, self.height = size

	def getSize(self):
		return self.width, self.height

	def setPosition(self, position):
		self.x, self.y = position

	def getPosition(self):
		return self.x, self.y

class LayoutBasicObject(GraphicBasicObject):
	def __init__(self, index, parent=None):
		super().__init__(index)
		self.parent = parent
		self.children = []

	def setParent(self, obj):
		if not obj is None:
			obj.children.append(self)
		self.parent = obj

	def addChild(self, obj):
		obj.setParent(self)




		