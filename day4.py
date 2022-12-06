

Example = "./Input/Example4.txt"
Input = "./Input/Input4.txt"

f = open(Input, 'r')

# part 1

result1 = 0
result2 = 0

for line in f.readlines():
    line = line.strip('\n')
    sects = line.split(',')
    sect1 = sects[0]
    sect2 = sects[1]

    start1 = int(sect1.split('-')[0])
    end1 = int(sect1.split('-')[1])

    start2 = int(sect2.split('-')[0])
    end2 = int(sect2.split('-')[1])

    # part 1 
    if start1 <= start2 and end1 >= end2:
        result1 +=1
    elif start2 <= start1 and end2 >= end1:
        result1 +=1

    # part 2

    if start2 <= end1 and end2 >= start1:
        print(f'{start2} <= {end1}')
        result2 +=1
    elif start1 <= end2 and end1 >= start2:
        print(f'{start1} <= {end2}')
        result2 +=1
    



print(f'Part1: {result1}')
print(f'Part2: {result2}')