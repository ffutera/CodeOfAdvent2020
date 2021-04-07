f = open("d8.txt", "r")
data = f.read().split("\n")
instructions = []
counter = 0
for d in data:
	items = d.split(" ")
	instructions.append((items[0],items[1],counter))
	counter+=1

flag = True
accum = 0
current_statement = instructions[0]
executed_instructions =  []
index =  0
termination = len(instructions)

def execute(param):
	global accum, executed_instructions, index
	#if (len(param)) !=3:
	#	print(param)
	task = param[0]
	value = param[1]
	counter = param[2]
	if task == "acc":
		accum+=int(value)
		index+=1
	elif task == "jmp":
		index+=int(value)
	else:
		index+=1
	executed_instructions.append((task,value,counter))
	if (index >= termination):
		return instructions[termination-1]
	return instructions[index]


for i in range(termination):
	accum=0
	current_statement=instructions[0]
	if instructions[i][0] == "jmp":
		instructions[i] = ("nop",instructions[i][1],instructions[i][2])
	elif instructions[i][0] == "nop":
		instructions[i] = ("jmp",instructions[i][1],instructions[i][2])
	else:
		continue
	condition = 0
	while(index!=(termination) and condition<50000):
		current_statement = execute(current_statement)
		#if (current_statement==instructions[termination-1]):
		#	print(instructions[i])
		#	print(index)
		#	break
		condition+=1
	if index == termination:
		print(instructions[i])
		print(index)
		break
	#print(current_statement)
#238 or 45?
print(accum)

