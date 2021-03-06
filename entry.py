import haversine

class Entry:
	def __init__(self, line):
		arr = line.split('|')
		self.name = arr[0]
		self.time = int(arr[1])
		self.lat = float(arr[2])
		self.lon = float(arr[3])

	def isInRange(self, other): 
		if (haversine.distance(self,other) <= 150):
			return True
		return False

	def isWithinSixHours(self, other):
		if abs((self.time - other.time)) <= (3600*6):
			return True
		return False

	def stringify(self):
		return self.name + " visited (" + str(self.lat) + "," + str(self.lon) + ") at " + str(self.time)

	def csvify(self):
		return self.name + "|" + str(self.time) + "|" + str(self.lat) + "|" + str(self.lon)