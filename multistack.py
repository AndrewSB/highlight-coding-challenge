import entry
import matchEntry

class MultiStack:
	def __init__(self):
		print "MultiStack created for data model"
		self.mainArray = []
		self.matchesArray = []

	def addStack(self, name):
		self.mainArray.append([name])
		return

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

		if not added:
			self.addStack(e.name)
			self.mainArray[-1].append(e)
			self.checkStacksForInteraction(e)
			return self.mainArray[-1][-1]

		return False

	def checkStacksForInteraction(self, e):
		for entryArray in self.mainArray:
			if not e.name == entryArray[0] and e.isInRange(entryArray[-1]):
				if e.isWithinSixHours(entryArray[-1]):
					return self.addToMatches(e, entryArray[-1])
				else:
					print "DIDN'T ADD " + matchEntry.MatchEntry(e, entryArray[-1]).stringify() + " because inactive" 

	def addToMatches(self, e, f):
		match = matchEntry.MatchEntry(e,f)
		if match.checkLastInteraction(self.matchesArray) < (24 * 60 * 60):
			print "DIDN'T ADD " + match.stringify() + " because less than 24 hours since last match"
		else:
			print "ADDED " + match.stringify()
			return self.matchesArray.append(match)

	def stringify(self):
		for entryArray in self.mainArray:
			for entry in entryArray:
				if entry != entryArray[0]:
					return entry.stringify()
				else:
					return entry