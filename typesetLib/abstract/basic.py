class ProofBasicObject(object):
	def __init__(self):
		self.userData = {}

	def setUserData(self, key, data):
		self.userData[key] = data

	def getUserData(self, key):
		return self.userData[key]

class TextFlowBasicObject(ProofBasicObject):
	def __init__(self, index=None):
		self.setIndex(index)

	def setIndex(self, index):
		self.index = index

	# def indexUP(self):
	# 	self.index += 1
	#
	# def indexDOWN(self):
	# 	NotImplemented

class GraphicBasicObject(TextFlowBasicObject):
	def __init__(self, size, index, position=None, verticalAlignment="top"):
		super().__init__(index)
		self.setSize(size)
		if position is not None:
			self.setPosition(position)
		self.setVerticalAlignment(verticalAlignment)

	def setSize(self, size):
		self.width, self.height = size

	def getSize(self):
		return self.width, self.height

	def setPosition(self, position):
		self.x, self.y = position

	def getPosition(self):
		return self.x, self.y

	def setVerticalAlignment(self, verticalAlignment):
		NotImplemented

class LayoutBasicObject(GraphicBasicObject):
	def __init__(self, size, index, parent=None, position=None, verticalAlignment="top"):
		super().__init__(size, index, position, verticalAlignment)
		self.parent = parent
		self.children = {}

	def setParent(self, obj):
		if not obj is None:
			if self.__class__.__name__ not in obj.children.keys():
				obj.children[self.__class__.__name__] = []
			obj.children[self.__class__.__name__].append(self)
		self.parent = obj

	def addChild(self, obj):
		#print(dir(obj))
		obj.setParent(self)




		