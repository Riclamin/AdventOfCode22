
class Tree:
    def __init__(self, height, visible):
        self.height = height
        self.visible = visible

    def __repr__(self):
        if self.visible:
            return f'[{self.height},v]'
        else:
            return f'[{self.height},i]'


Example = "./Input/Example8.txt"
Input = "./Input/Input8.txt"

f = open(Input, 'r')



# part 1

lines = f.readlines()
trees = [] # list of lists of Trees. trees[i][j] will return row i, col j

maxRows = len(lines)
maxCols = len(lines[0]) -1 #Remove \n character from length.

# Check visibility in rows.
for line in lines:
    line = line.strip('\n')
    treeRow = []

    maxHeightSeen = 0
    for i in range(maxCols): # check if tree is visible from left to right
        height = int(line[i])
        if line == lines[0].strip('\n') or line == lines[maxRows-1].strip('\n'): # all trees in the first and last row are visible
            treeRow.append(Tree(height, True))
        elif height > maxHeightSeen:
            maxHeightSeen = height
            treeRow.append(Tree(height, True))
        else:
            treeRow.append(Tree(height, False))

    maxHeightSeen = 0
    for tree in treeRow[::-1]: # check if tree is visible from right to elft
        height = tree.height
        if height > maxHeightSeen:
            maxHeightSeen = height
            tree.visible = True
        if height == 9:
            break
    
    trees.append(treeRow)


for col in range(maxCols):
    treeCol = []
    for row in range(maxRows):
        treeCol.append(trees[row][col])
    
    if col == 0 or col == maxCols -1:
        for tree in treeCol:
            tree.visible = True
    
    maxHeightSeen = 0
    for tree in treeCol: # check if tree is visible from top to bottom
        height = tree.height
        if height > maxHeightSeen:
            maxHeightSeen = height
            tree.visible = True
        if height == 9:
            break
    
    maxHeightSeen = 0
    for tree in treeCol[::-1]: # check if tree is visible from bottom to top
        height = tree.height
        if height > maxHeightSeen:
            maxHeightSeen = height
            tree.visible = True
        if height == 9:
            break

# Checked for visibility on all trees.


visibleTrees = 0

for row in trees:
    for tree in row:
        if tree.visible:
            visibleTrees+=1

# print(trees)
print(f'There are {visibleTrees} visible from the outside.')

# Part 2

highestScenicScore = 0
for row in range(maxRows):
    for col in range(maxCols): # Iterating over all trees in the matrix.
        currentScenicScore = 1
        if row == 0 or row == maxRows-1 or col == 0 or col == maxCols -1: #it's somewhere on the edge; ignore the tree.
            currentScenicScore = 0
            continue
        else:   # it's one of the middle trees: 
            tree = trees[row][col]
            height = tree.height

            indexR = trees[row].index(tree) #Find tree so we can look to the trees on the right.
            right = 1
            while (indexR+right) < (maxCols-1) and trees[row][indexR+right].height < height:
                right +=1
            
            reverseRow = trees[row][::-1] #Find tree in the reverse of the row so we can look to the trees on the left.
            indexL = reverseRow.index(tree)
            left = 1
            while (indexL+left) < (maxCols-1) and reverseRow[indexL+left].height < height:
                left +=1
            
            treeCol = [] # Make a list with all the trees in that column.
            for tempRow in range(maxRows):
                treeCol.append(trees[tempRow][col])
            
            
            indexB = treeCol.index(tree)
            bot = 1
            while (indexB+bot) < (maxRows-1) and treeCol[indexB+bot].height < height:
                bot+=1

            reverseCol = treeCol[::-1] #Find tree in the column of trees so we can look to trees to the bottom.
            indexT = reverseCol.index(tree) #Find tree in the reverse of the column of trees so we can look to trees to the top.
            top = 1
            while (indexT+top) < (maxRows-1) and reverseCol[indexT+top].height < height:
                top+=1
            
            currentScenicScore*= left * right * top * bot # Determine the scenic score for this tree. 
            if currentScenicScore > highestScenicScore: #update highest score if the currents core is higher.
                highestScenicScore = currentScenicScore
            # print(f'Considering tree at ({row},{col}). Scenic score is determined as: {right}*{left}*{bot}*{top}= {currentScenicScore}. Highest score so far is: {highestScenicScore}.')

print(f'The highest scenic score that was found is: {highestScenicScore}')
        



# Parsed all input/output

