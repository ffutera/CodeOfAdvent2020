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
		newList.append((" ".join(requiredData),elements[0]))
		if newList == [('other bags.','no')]:
			newList = []
	dictionary[combo[0]] = newList

def getBags(bag):
	li = dictionary[bag]
	if not li:
		return 0
	sum = 0
	for b in li:
		sum+=int(b[1])*(getBags(b[0])) + int(b[1])
	return sum

value = getBags("shiny gold")
print(value)

