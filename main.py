from __future__ import print_function
import entry
import multistack


ms = multistack.MultiStack()
for line in open("userdata.txt", 'r'):
	if not ms.addEntry(entry.Entry(line)):
		print("ERROR: could not check" + line + " for some reason.")

print("\n\n\n\nFINAL OUTPUT___________________________________________________________________")

writeFile = open("results.txt", 'w')
for result in ms.matchesArray:
	print(result.stringify())
	print(result.csvify(), file=writeFile)