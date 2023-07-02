class ProofBasicObject(object):
	def __init__(self):
		self.userData = {}

	def setUserData(self, key, data):
		self.userData[key] = data

	def getUserData(self, key):
		return self.userData[key]

class TextFlowBasicObject(ProofBasicObject)
	def __init__(self, index):
		self.index = index

	def indexUP(self):
		self.index += 1

	def indexDOWN(self):
		NotImplemented

class LayoutBasicObject(TextFlowBasicObject):
	def __init__(self, index, parent=None):
		super().__init__(index)
		self.parent = parent
		self.children = []

	def setParent(self, obj):
		if obj not is None:
			obj.children.append(self)
		self.parent = obj

	def addChild(self, obj):
		obj.setParent(self)




		