
Example = "./Input/Example6.txt"
Input = "./Input/Input6.txt"

f = open(Input, 'r')



# part 1

lines = f.readlines()

# print(lines)
for line in lines:
    line = line.strip('\n')

    i = 3
    while i < len(line):
        marker = set()
        marker.add(line[i-3])
        marker.add(line[i-2])
        marker.add(line[i-1])
        marker.add(line[i])
        

        if len(marker) == 4:
            break;
        i+=1
    print(f'Marker received at character: {i+1}')

for line in lines:
    line = line.strip('\n')

    i = 0
    list = []
    while i < 13:
        list.append(line[i])
        i+=1
    
    while i < len(line):
        list.append(line[i])
        # print(f'considering letter {line[i]}')
        marker = set()
        marker.update(list)
        
        print(marker)
        if len(marker) == 14:
            break;
        list= list[1:]
        i+=1

    print(f'Start of Message marker received at character: {i+1}')
# print(f'Marker received at character: {i+1}')