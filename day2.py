

Example = "./Input/2_Example.txt"
Input = "./Input/2_Input.txt"

f = open(Input, 'r')

# part 1

# C1 = Enemy, C2 = My play;
# A = Rock, B = Paper, C = Scissor
# X = Rock, Y = Paper, Z = Scissor
# L = 0, D = 3, W = 6
# X = 1, Y = 2, Z = 3
scenarios = [("A X", 4), ("A Y", 8), ("A Z", 3)
            ,("B X", 1), ("B Y", 5), ("B Z", 9)
            ,("C X", 7), ("C Y", 2), ("C Z", 6)]

values = {}
for (a,b) in scenarios:
    values[a] = b


# C1 = Enemy, C2 = Result;
# A = Rock, B = Paper, C = Scissor
# X = Lose, Y = Draw, Z = Win
# R = 1, P = 2, S = 3
# X = 0, Y = 3, Z = 6
scenarios2 =[("A X", 3), ("A Y", 4), ("A Z", 8)
            ,("B X", 1), ("B Y", 5), ("B Z", 9)
            ,("C X", 2), ("C Y", 6), ("C Z", 7)]
values2 = {}
for (a,b) in scenarios2:
    values2[a] = b


score = 0
score2 = 0


for line in f.readlines():
    line = line.strip('\n')
    # print(line)
    score += values[line]
    score2 += values2[line]

print(f'Part 1: {score}')
print(f'Part 2: {score2}')
