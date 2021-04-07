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


def execute(param):
	task = param[0]
	value = param[1]
	counter = param[2]
	global accum, executed_instructions, index
	if task == "acc":
		accum+=int(value)
		index+=1
	elif task == "jmp":
		index+=int(value)
	else:
		index+=1
	executed_instructions.append((task,value,counter))
	return instructions[index]

while(current_statement not in executed_instructions):
	current_statement = execute(current_statement)
	print(current_statement)

print(accum)


