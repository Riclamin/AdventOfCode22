

Example = "./Input/1_Example.txt"
Input = "./Input/1_Input.txt"

f = open(Input, 'r')


elves ={}
elfCounter = 1
for line in f.readlines():
    line = line.strip('\n')
    print(line)

    if len(line) > 0:
        if elfCounter in elves:
            elves[elfCounter] += int(line)
        else:
            elves[elfCounter] = int(line)
    else:
        elfCounter+= 1

# print(elves)

pair = (0,0)
for key in elves:
    if elves[key] > pair[1]:
        pair = (key,elves[key])

print(pair)

elflist = []

for key in elves:
    elflist.append((key, elves[key]))

elflist.sort(key = lambda x: x[1], reverse=True)
print(elflist)