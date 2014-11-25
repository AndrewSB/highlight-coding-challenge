import haversine

class Entry:
	def __init__(self, line):
		arr = line.split('|')
		self.name = arr[0]
		self.time = int(arr[1])
		self.lat = float(arr[2])
		self.lon = float(arr[3])

	def stringify(self):
		return self.name + " visited (" + str(self.lat) + "," + str(self.lon) + ") at " + str(self.time)

	def isInRange(self, other): 
		delta = haversine.distance(self,other)
		print delta
		if (delta < 150.000000001):
			return True
		return False