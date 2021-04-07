f = open("d9.txt","r")
data = f.read().split("\n")
data = [int(d) for d in data]	
value = 2089807806

for i in range(0,len(data)):
	counter = 0
	s = 0
	while (s<value):
		s+=int(data[i+counter])
		counter+=1
	if s==value:
		print(min(data[i:i+counter])+max(data[i:i+counter]))
		break

