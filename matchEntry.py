import entry
import haversine

class matchEntry(entry): #matchEntry extends entry
	def __init__(self, e, f):
		self.time = e.time if e.time > f.time else f.time

		self.name1 = e.name if e.name < f.name else f.name
		self.lat1 = e.lat if e.name < f.name else f.lat
		self.lon1 = e.lon if e.name < f.name else f.lon

		self.name2 = e.name if e.name > f.name else f.name
		self.lat2 = e.lat if e.name > f.name else f.lat
		self.lon2 = e.lon if e.name > f.name else f.lon

		self.differential = haversine.distance(e,f)

	def stringify(self):
		return name1 + " met " + name2 + " at " str(self.time) + " with a distance differential of " + str(self.differential) 

	def csvify(self):
		return self.name + "|" + str(self.time) + "|" + str(self.lat) + "|" + str(self.lon)