f = open("bags.txt", "r")
data = f.read().split("\n")
l = []
for d in data:
	s = d.split(" bags contain ")
	l.append(s)

dictionary = {}
for combo in l:
	contain = combo[1]
	li = contain.split(", ")
	newList = []
	for item in li:
		elements = item.split(" ")
		requiredData = elements[1:3]
		newList.append(" ".join(requiredData))
		if newList == ['other bags.']:
			newList = []
	dictionary[combo[0]] = newList



bags = ["shiny gold"]
foundNew = True
while (foundNew):
	foundNew = False
	for (key,value) in dictionary.items():
		if any(x in value for x in bags):
			if not key in bags:
				bags.append(key)
				foundNew = True

print(len(bags)-1)

#use (bagname,number) tupples for part 2
