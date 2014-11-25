import entry

class MultiStack:
	def __init__(self):
		print "multi stack created"
		self.mainArray = []

	def addEntry(self, entry):
		i = 0
		for entryArray in self.mainArray:
			if entry.name == entryArray[0]:
				self.mainArray[i].append(entry)
			i+=1



	def addStack(self, name):
		name = ["name"]
		self.mainArray.append(["name"])


	def stringify(self):
		for entryArray in self.mainArray:
			print "New entryArray"
			for entry in entryArray:
				print entry


ms = MultiStack()
ms.addEntry(entry.Entry("unclejoey|1327430121|37.777372247259|-122.3981163202"))
ms.addEntry(entry.Entry("unclejoey|1327437628|37.777253789662|-122.3981738187"))

ms.stringify()
