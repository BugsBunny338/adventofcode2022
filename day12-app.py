mapp = []

def printMap():
    for line in mapp:
        print(''.join(line))

def getDistance(distances, coords):
    if distances.get(coords) == None:
        return '∞' # float('inf')
    else:
        return distances[coords]

def printDistances(distances):
    for y, row in enumerate(mapp):
        line = []
        for x in range(len(mapp[0])):
            coords = f'{x}-{range(len(mapp))[-y-1]}'
            line.append(f'{coords}: {mapp[y][x]} ({getDistance(distances, coords)})')
        print(line)

def getCoordsOf(ch):
    allCoords = []
    for y, row in enumerate(mapp):
        for x in range(len(mapp[0])):
            coords = f'{x}-{range(len(mapp))[-y-1]}'
            if mapp[y][x] == ch:
                allCoords.append(coords)
    return allCoords

def getCharAt(x, y):
    return mapp[range(len(mapp))[-y-1]][x]

def getNeighborsFrom(x, y):
    neighborSquares = []
    if x > 0:
        # left
        neighborSquares.append(f'{x-1}-{y}')
    if y > 0:
        # down
        neighborSquares.append(f'{x}-{y-1}')
    if x < len(mapp[0]) - 1:
        # right
        neighborSquares.append(f'{x+1}-{y}')
    if y < len(mapp) - 1:
        # up
        neighborSquares.append(f'{x}-{y+1}')
    return neighborSquares

def getAccessibleSquaresFrom(x, y):
    neighborSquares = getNeighborsFrom(x, y)
    fromChar = getCharAt(x, y)
    accessibleSquares = []
    for sq in neighborSquares:
        [x, y] = map(int, sq.split('-'))
        # print(x, y)
        toChar = getCharAt(x, y)
        if (toChar != 'E' and ord(toChar) - ord(fromChar) <= 1) or fromChar == 'S' or (fromChar == 'z' and toChar == 'E'):
            accessibleSquares.append(sq)
            # print(f'{fromChar} > {toChar}')
    return accessibleSquares

def exploreFrom(s):
    squaresToExplore = [s]
    distances = { s: 0 }
    while len(squaresToExplore):
        sq = squaresToExplore.pop(0)
        sqDistance = distances[sq]
        [sqX, sqY] = map(int, sq.split('-'))
        # print(f'Exploring                {sqX}-{sqY} ({getCharAt(sqX, sqY)})')
        accessibleSquares = getAccessibleSquaresFrom(sqX, sqY)
        # print(f'Accesible squares: {", ".join(accessibleSquares)}')
        for nextSquare in accessibleSquares:
            [nextSqX, nextSqY] = map(int, nextSquare.split('-'))
            # print(f' Accessible square       {nextSquare} ({getCharAt(nextSqX, nextSqY)})')
            if distances.get(nextSquare) == None:
                distances[nextSquare] = sqDistance + 1
                # print(f'  Previous distance to   {nextSquare} ({getCharAt(nextSqX, nextSqY)}) was unknown')
                # print(f'  New distance to        {nextSquare} ({getCharAt(nextSqX, nextSqY)}) is {distances[nextSquare]}')
                squaresToExplore.append(nextSquare)
            else:
                prevDistance = distances[nextSquare]
                # print(f'  Previous distance to   {nextSquare} ({getCharAt(nextSqX, nextSqY)}) was {prevDistance}')
                if prevDistance > sqDistance + 1:
                    distances[nextSquare] = sqDistance + 1
                    # print(f'  New distance to        {nextSquare} ({getCharAt(nextSqX, nextSqY)}) is {distances[nextSquare]}')
                    squaresToExplore.append(nextSquare)
                else:
                    # print(f'  New distance to        {nextSquare} ({getCharAt(nextSqX, nextSqY)}) remains {prevDistance}')
                    pass
    return distances

with open('day12-input.txt') as f:
    for line in f:
        mapp.append([])
        for ch in line.strip():
            mapp[-1].append(ch)

# printMap()
# s = getCoordsOf('S')[0]
# e = getCoordsOf('E')[0]
# distances = exploreFrom(s)
# printDistances(distances)
# print(getDistance(distances, e))

aa = getCoordsOf('a')
e = getCoordsOf('E')[0]
results = []
for a in aa:
    distances = exploreFrom(a)
    distance = getDistance(distances, e)
    # print(distance)
    if distance != '∞':
        results.append(distance)

print(min(results))
