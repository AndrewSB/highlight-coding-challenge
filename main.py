from __future__ import print_function
import entry
import multistack


ms = multistack.MultiStack()
for line in open("userdata.txt", 'r'):
	ms.addEntry(entry.Entry(line))

results = ms.matchesArray
writeFile = open("output.txt", 'w')
for result in results:
	print(result.stringify())
	print(result.csvify(), file=writeFile)