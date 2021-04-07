import string
import re
#Gives one valid passport too many for some reason? Possible simple bug
file = "d4.txt"
i = 0
data = []
for line in open(file):
    data.append(line.rstrip())

rawindices = []
for i in range(len(data)):
    if data[i] == '':
        rawindices.append(i)

indices=[]
for i in range(len(rawindices)-1):
    indices.append((rawindices[i],rawindices[i+1]))

indices.append((rawindices[len(rawindices)-1],(len(data)+1)))

d=[]
d[0:rawindices[0]] = [''.join(data[0 : rawindices[0]])] 
#print(d)
for (x,y) in indices:
    d.append(''.join(data[x+1:y]))

validcount = 0
for item in d:
    valid=False
    item = item.replace(' ','')
    if (item.count(':') == 8 or ("cid" not in item and item.count(':') == 7)):
        colonindex = [pos for pos, char in enumerate(item) if char == ':']
        valid = True
        for index in colonindex:
            identifier = item[index-3:index]
            if (identifier == 'pid'):
                value = item[index+1:index+10]
                if not bool(re.match("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",value)):
                    valid = False
                    print(value, " - 9 digit number")
            if (identifier == 'ecl'):
                value = item[index+1:index+4]
                if not ( value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    valid = False
                    print(value, " - amb blu brn gry grn hzl oth")
                #print(identifier," ",value," ",valid)
            if (identifier == 'hcl'):
                value = item[index+1:index+8]
                if not (bool(re.match("#[0-f][0-f][0-f][0-f][0-f][0-f]",value))):
                    valid = False
                    print(value, " - # and 6 characters")
                #print(identifier," ",value," ",valid)
            if (identifier == 'byr'):
                value = int(item[index+1:index+5])
                if not (1920<=value and value<=2002):
                    valid = False
                    print(value, " - 1920-2002")
                #print(identifier," ",value," ",valid)
            if (identifier == 'eyr'):
                value = int(item[index+1:index+5])
                if not (2020<=value and value<=2030):
                    valid = False
                    print(value, " - 2020-2030")
                #print(identifier," ",value," ",valid)
            if (identifier == 'hgt'):
                height = item[index+1:index+6]
                if not (bool(re.match("(1[5-8][0-9]cm)",height))
                        or bool(re.match("19[0-3]cm", height))
                        or bool(re.match("7[0-6]in",height))
                        or bool(re.match("59in",height))
                        or bool(re.match("6[0-9]in",height))):
                    valid = False
                    print(height, " - 150-193cm or 59-76inch")
                #print(identifier," ",height," ",valid)
            if (identifier == 'iyr'):
                value = int(item[index+1:index+5])
                if not (2010<=value and value<=2020):
                    valid = False
                    print(value, " - 2010-2020")
                #print(identifier," ",value," ",valid)
            #if (identifier == 'cid'):
            #    pass
    if valid:
        validcount+=1

print(validcount)
