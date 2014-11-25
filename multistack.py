import entry

class MultiStack:
	def __init__(self):
		print "multi stack created"
		self.mainArray = []

	def addEntry(self, e):
		i = 0
		added = False
		for entryArray in self.mainArray:
			if e.name == entryArray[0]:
				self.mainArray[i].append(e)
				added = True
				return self.mainArray[i][-1]
			i+=1
		i = 0
		if not added:
			self.addStack(e.name)
			self.mainArray[-1].append(e)
			return self.mainArray[-1][-1]
		return False



	def addStack(self, name):
		self.mainArray.append([name])


	def stringify(self):
		for entryArray in self.mainArray:
			for entry in entryArray:
				if entry != entryArray[0]:
					print entry.stringify()
				else:
					print entry


# ms = MultiStack()
# ms.addEntry(entry.Entry("unclejoey|1327430121|37.777372247259|-122.3981163202"))
# ms.addEntry(entry.Entry("jj|1327437628|37.777253789662|-122.3981738187"))
# ms.addEntry(entry.Entry("danny|1327428557|37.77723932161|-122.39818298999"))
# ms.addEntry(entry.Entry("danny|1327428557|37.77723932161|-122.39818298999"))
# ms.addEntry(entry.Entry("unclejoey|1327430121|37.777372247259|-122.3981163202"))


# ms.stringify()
