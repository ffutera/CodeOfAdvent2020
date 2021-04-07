f = open("d9.txt","r")
data = f.read().split("\n")

def isSumable(value, numbers):
	for i in range(25):
		target = int(value)-int(numbers[i])
		if str(target) in numbers[:i] + numbers[i+1:]:
			return True
	return False

for i in range(25,len(data)):
	previous = data[i-25:i]
	if not isSumable(data[i],previous):
		print(data[i])
		break

