class ProofBasicObject(object):
	def __init__(self):
		self.userData = {}

	def setUserData(self, key, data):
		self.userData[key] = data

	def getUserData(self, key):
		return self.userData[key]

		