
def moveCrate1(stacks, number, src, dst):
    src-= 1
    dst-= 1

    while number > 0:
        crate = stacks[src].pop()
        stacks[dst].append(crate)
        number -=1
    return stacks

def moveCrate2(stacks, number, src, dst):
    src-=1
    dst-=1
    crates = []
    while number > 0:
        crates.append(stacks[src].pop())
        number -=1

    crates.reverse()
    for crate in crates:
        stacks[dst].append(crate)

    return stacks



# Update the input files so that each initial stack is contained one line for easier to read out.

Example = "./Input/Example5.txt"
Input = "./Input/Input5.txt"

f = open(Input, 'r')



# part 1

stacks = []

index = 0

lines = f.readlines()

while (lines[index] != "\n"):
    stack = []
    line = lines[index].strip('\n').split(' ')[1]
    for char in line:
        stack.append(char)
    stacks.append(stack)
    index+=1

print(stacks)

index +=1

for line in lines[index:]:
    line = line.strip('\n').split(' ')
    stacks = moveCrate2(stacks, int(line[1]), int(line[3]), int(line[5]))



print(stacks)
    
result = ""

for stack in stacks:
    result+= stack.pop()

print(result)


# print(f'Part1: {result1}')
# print(f'Part2: {result2}')