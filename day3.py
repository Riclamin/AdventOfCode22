


def priority(char):
    list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return list.index(char) +1


Example = "./Input/Example3.txt"
Input = "./Input/Input3.txt"

f = open(Input, 'r')

# part 1

result = []

for line in f.readlines():
    line = line.strip('\n')

    nrItems = len(line)
    
    set1 = set()
    set2 = set()
    for char in line[:int(nrItems/2)]:
        set1.add(char)
    for char in line[int(nrItems/2):]:
        set2.add(char)

    # print(f'{set1=}')
    # print(f'{set2=}')

    result.append((set1 & set2).pop())
    # print(line)

# print(result)

priorities = []
for char in result:
    priorities.append(priority(char))

# print(priorities)
# print(sum(priorities))


# Part 2:

f.close()
f = open(Input, 'r')

lines = f.readlines()

badges = []
for i in range(int(len(lines)/3)):

    index = i*3 
    rucksack1 = set()
    rucksack2 = set()
    rucksack3 = set()
    lines[index] = lines[index].strip('\n')
    lines[index+1] = lines[index+1].strip('\n')
    lines[index+2] = lines[index+2].strip('\n')
    for char in lines[index]:
        rucksack1.add(char)
    for char in lines[index+1]:
        rucksack2.add(char)
    for char in lines[index+2]:
        rucksack3.add(char)
    
    badge = (rucksack1 & rucksack2 & rucksack3).pop()
    badges.append(badge)

badgesPriorities = []

for b in badges:
    badgesPriorities.append(priority(b))

print(badges)
print(badgesPriorities)
print(sum(badgesPriorities))