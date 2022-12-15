map = []
rowNum = 0
colNum = 0
visibleTrees = 0
maxScore = 0

def getVisibility(r, c, value):
    visibleFromBottom = True
    for down in range(r + 1, rowNum):
        # print('down', down, map[down][c])
        if value <= map[down][c]:
            visibleFromBottom = False
    visibleFromTop = True
    for up in range(r - 1, -1, -1):
        # print('up', up, map[up][c])
        if value <= map[up][c]:
            visibleFromTop = False
    visibleFromRight = True
    for right in range(c + 1, colNum):
        # print('right', right, map[r][right])
        if value <= map[r][right]:
            visibleFromRight = False
    visibleFromLeft = True
    for left in range(c - 1, -1, -1):
        # print('left', left, map[r][left])
        if value <= map[r][left]:
            visibleFromLeft = False
    if visibleFromBottom or visibleFromTop or visibleFromRight or visibleFromLeft:
        return 1
    else:
        return 0

def getScore(r, c, value):
    scoreFromBottom = 0
    for down in range(r + 1, rowNum):
        # print('down', down, map[down][c])
        if value > map[down][c]:
            scoreFromBottom += 1
        else:
            scoreFromBottom += 1
            break
    scoreFromTop = 0
    for up in range(r - 1, -1, -1):
        # print('up', up, map[up][c])
        if value > map[up][c]:
            scoreFromTop += 1
        else:
            scoreFromTop += 1
            break
    scoreFromRight = 0
    for right in range(c + 1, colNum):
        # print('right', right, map[r][right])
        if value > map[r][right]:
            scoreFromRight += 1
        else:
            scoreFromRight += 1
            break
    scoreFromLeft = 0
    for left in range(c - 1, -1, -1):
        # print('left', left, map[r][left])
        if value > map[r][left]:
            scoreFromLeft += 1
        else:
            scoreFromLeft += 1
            break
    # print(scoreFromBottom, scoreFromTop, scoreFromLeft, scoreFromRight)
    return scoreFromBottom * scoreFromTop * scoreFromLeft * scoreFromRight

with open('day08-input.txt') as f:
    for line in f:
        map.append([])
        for ch in line.strip():
            map[-1].append(int(ch))

colNum = len(map)
rowNum = len(map[0])

for r, row in enumerate(map):
    if r != 0 and r != len(map)-1:
        for c, value in enumerate(row):
            if c != 0 and c != len(row)-1:
                # print(value)
                # print(r, c, value)
                visibleTrees += getVisibility(r, c, value)
                score = getScore(r, c, value)
                if score > maxScore:
                    maxScore = score

# print(getVisibility(1, 1, 5))
# print(getVisibility(1, 2, 5))
# print(getVisibility(1, 3, 1))
# print(getVisibility(2, 3, 3))

print(visibleTrees + 2 * colNum + 2 * (rowNum - 2))

# print(getScore(1, 2, 5))
# print(getScore(3, 2, 5))

print(maxScore)
