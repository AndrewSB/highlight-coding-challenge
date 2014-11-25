import entry

class MultiStack:
	def __init__(self):
		print "multi stack created"
		self.mainArray = []
		self.matchesArray = []

	def addStack(self, name):
		self.mainArray.append([name])

	def addEntry(self, e):
		i = 0
		added = False
		for entryArray in self.mainArray:
			if e.name == entryArray[0]:
				self.mainArray[i].append(e)
				added = True
				self.checkStacksForInteraction(e)
				return self.mainArray[i][-1]
			i+=1
		i = 0
		if not added:
			self.addStack(e.name)
			self.mainArray[-1].append(e)
			self.checkStacksForInteraction(e)
			return self.mainArray[-1][-1]
		return False

	def checkStacksForInteraction(self, e):
		print "check "+e.stringify()
		for entryArray in self.mainArray:
			if not e.name == entryArray[0]:
				if e.isInRange(entryArray[-1]):
					if e.isWithinSixHours(entryArray[-1]):
						print "hit with " + entryArray[-1].stringify()

	def stringify(self):
		for entryArray in self.mainArray:
			for entry in entryArray:
				if entry != entryArray[0]:
					print entry.stringify()
				else:
					print entry


ms = MultiStack()
ms.addEntry(entry.Entry("unclejoey|1327430121|37.777372247259|-122.3981163202"))
ms.addEntry(entry.Entry("jj|1327451720|37.777253789662|-122.3981738187"))