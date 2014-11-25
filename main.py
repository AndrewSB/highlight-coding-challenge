import entry
import multistack

def readData(filename):
	file = open(filename, 'r')
	for line in file:
		print entry.Entry(line).stringify()

readData("userdata.txt")