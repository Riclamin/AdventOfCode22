
class Directory:
    # files are assumed to be tuples of (size:int, name:str)
    
    def __init__(self,  parent, name):
        self.parent = parent        # parent directory
        self.name = name            # name of this directory
        self.subDirectories = []    # list of names of directories inside this directory
        self.files = []             # lsit of 
        self.size = 0

    def __repr__(self):
        if self.name == '/':
            return f'(Parent: {None}, name: {self.name}, subDirectories: {self.subDirectories}, files: {self.files}, size: {self.size})'
        else:
            return f'(Parent: {self.parent.name}, name: {self.name}, subDirectories: {self.subDirectories}, files: {self.files}, size: {self.size})'
        
    
    def addSubDirectory(self, dir):
        self.subDirectories.append(dir)
        self.size += dir.size
        
    def updateParentSize(self, parent, size):
        if self.parent is not None:
            self.parent.size += size
            parent.updateParentSize(parent.parent, size)

    def addFile(self, file):
        self.files.append(file)
        self.size += file[0]
        self.updateParentSize(self.parent, file[0])
            




def findSmallDirs(maxSize, dir: Directory):
    result = []
    for subDir in dir.subDirectories:
        smallSubDirs = findSmallDirs(maxSize, subDir)
        for smallSubDir in smallSubDirs:
            result.append(smallSubDir)
    if dir.size < maxSize:
        result.append(dir)
    return result

def addDirSizes(dirs):
    result = 0
    for dir in dirs:
        result+= dir.size
    return result

def findSmallestDir(minSize, dir: Directory):
    smallestDir = None
    for subDir in dir.subDirectories:
        smallestSubDir = findSmallestDir(minSize, subDir)
        if smallestDir is None:
            smallestDir = smallestSubDir
        elif smallestSubDir is None:
            continue        
        elif smallestSubDir.size < smallestDir.size:
            smallestDir = smallestSubDir
    
    if smallestDir is None and dir.size > minSize:
        return dir
    else:
        return smallestDir

Example = "./Input/Example7.txt"
Input = "./Input/Input7.txt"

f = open(Input, 'r')



# part 1

lines = f.readlines()

root = Directory(None, '/')
curDir = root

# print(lines)
for line in lines:
    line = line.strip('\n').split(' ')
    print(line)
    
    if line[0] == '$':
        # it's a command: 
        if line[1] == 'cd':
            if line[2] == '..':
                curDir = curDir.parent
            else:
                for subDir in curDir.subDirectories:
                    if subDir.name == line[2]:
                        curDir=subDir
                        continue
        elif line[1] == 'ls':
            continue


    else:
        # it's output:
        if line[0] == 'dir':
            subDir = Directory(curDir, line[1])
            curDir.addSubDirectory(subDir)
        elif line[0].isdigit():
            curDir.addFile((int(line[0]), line[1]))
    print(curDir)

# Parsed all input/output

# Find directories where size < 100 000:

smallDirs = findSmallDirs(100000, root)

print(f'Small directories are: {smallDirs}')
print(f'Total size of small directories is: {addDirSizes(smallDirs)}')

print(f'root is: {root}')

neededSpace = 30000000 - (70000000 - root.size)
print(f'needed space is: {neededSpace}')
smallestDir = findSmallestDir(neededSpace, root)
print(f'smallest dir = {smallestDir}')
