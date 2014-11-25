import haversine

class MatchEntry():
	def __init__(self, e, f):
		self.time = e.time if e.time > f.time else f.time

		self.name1 = e.name if e.name < f.name else f.name
		self.lat1 = e.lat if e.name < f.name else f.lat
		self.lon1 = e.lon if e.name < f.name else f.lon

		self.name2 = e.name if e.name > f.name else f.name
		self.lat2 = e.lat if e.name > f.name else f.lat
		self.lon2 = e.lon if e.name > f.name else f.lon

		self.differential = haversine.distance(e,f)

	def checkLastInteraction(self, mArray):
		relArray = []
		returnArray = []
		for m in mArray:
			if self.name1 == m.name1 and self.name2 == m.name2:
				relArray.append(m)

		for r in relArray:
			returnArray.append(r.time)

		return abs(max(returnArray) - self.time) if returnArray else ((24 * 60 * 60) + 1)


	def stringify(self):
		return self.name1 + " met " + self.name2 + " at " + str(self.time) + " with a distance differential of " + str(self.differential) 

	def csvify(self):
		return self.time + "|" + self.name1 + "|" + str(self.lat1) + "|" + str(self.lon1) + "|" + self.name2 + "|" + str(self.lat2) + "|" + str(self.lon2)