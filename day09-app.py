import itertools

instructions = ['s']
headPositions = [[0, 0]]
tailsPositions = [[[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]

def getNewTailPos(headPos, tailPos):
    headX = headPos[0]
    headY = headPos[1]
    tailX = tailPos[0]
    tailY = tailPos[1]
    if abs(headX - tailX) >= 2 and abs(headY - tailY) >= 2:
        if headX > tailX and headY > tailY:
            return [tailX + 1, tailY + 1]
        if headX < tailX and headY < tailY:
            return [tailX - 1, tailY - 1]
        if headX > tailX and headY < tailY:
            return [tailX + 1, tailY - 1]
        if headX < tailX and headY > tailY:
            return [tailX -1, tailY + 1]
    if abs(headX - tailX) >= 2:
        if headX > tailX:
            return [tailX + 1, headY]
        if headX < tailX:
            return [tailX - 1, headY]
    if abs(headY - tailY) >= 2:
        if headY > tailY:
            return [headX, tailY + 1]
        if headY < tailY:
            return [headX, tailY - 1]
    return [tailX, tailY]

def getUniquePositions(positions):
    # https://stackoverflow.com/a/2213973/1881978
    sortedPositions = list(positions)
    sortedPositions.sort()
    return list(sortedPositions for sortedPositions,_ in itertools.groupby(sortedPositions))

with open('day09-input.txt') as f:
    for line in f:
        instruction = line.strip().split()
        # print(instruction)
        direction = instruction[0]
        movesCount = int(instruction[1])
        # print(direction, movesCount)
        for i in range(movesCount):
            instructions.append(direction)
            lastHeadPos = headPositions[-1]
            match direction:
                case 'U':
                    headPositions.append([lastHeadPos[0], lastHeadPos[1] + 1])
                case 'R':
                    headPositions.append([lastHeadPos[0] + 1, lastHeadPos[1]])
                case 'D':
                    headPositions.append([lastHeadPos[0], lastHeadPos[1] - 1])
                case 'L':
                    headPositions.append([lastHeadPos[0] - 1, lastHeadPos[1]])
            for j in range(len(tailsPositions)):
                prevTailPositions = headPositions if j == 0 else tailsPositions[j - 1]
                tailsPositions[j].append(getNewTailPos(prevTailPositions[-1], tailsPositions[j][-1]))

for i, pos in enumerate(headPositions):
    print(
        i if i > 9 else '0' + str(i),
        instructions[i],
        'H:' + str(pos),
        '1:' + str(tailsPositions[0][i]),
        '2:' + str(tailsPositions[1][i]),
        '3:' + str(tailsPositions[2][i]),
        '4:' + str(tailsPositions[3][i]),
        '5:' + str(tailsPositions[4][i]),
        '6:' + str(tailsPositions[5][i]),
        '7:' + str(tailsPositions[6][i]),
        '8:' + str(tailsPositions[7][i]),
        '9:' + str(tailsPositions[8][i])
    )

# print(headPositions)
# print(tailsPositions[0])
print(len(getUniquePositions(tailsPositions[-1])))
