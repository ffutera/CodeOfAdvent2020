f = open("d6.txt", "r")
#data = f.read().split("\n\n")

#length = 0
#for item in data:
#    s = set(item)
#    if ('\n' in s):
#        s.remove('\n')
#    length+=len(s)

#print(length)
length = 0
data = f.read().split("\n\n")
for item in data:
    li = item.split("\n")
    chars = []
    for c in li[0]:
        elem = True
        for i in li:
            if c not in i:
                elem = False
        if elem:
            chars.append(c)
    length+=len(chars)
