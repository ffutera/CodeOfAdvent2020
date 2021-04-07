f = open("d10.txt","r")
data = [int(d) for d in f.read().split("\n")]
data.append(max(data)+3) #to account for devices power foltage
difference = [0,0,0]
charge = 0
target = len(data)
while (sum(difference)<target):
	for delta in range(1,4):
		found = False
		for d in data:
			if d == charge+delta:
				difference[delta-1]+=1
				data.remove(d)
				charge+=delta
				found = True
				break
		if found:
			break
print(difference[0]*difference[2])
