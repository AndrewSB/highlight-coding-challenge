import entry


e = entry.Entry("danny|1327401809|37.775011290418|-122.39381636393")
print e.stringify()

f = entry.Entry("danny|1327401809|37.775011290418|-122.39381636393")

print e.isInRange(f)