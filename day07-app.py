path = []
sizes = {}
capacity = 70000000
neededSpace = 30000000

with open('day07-input.txt') as f:
    for line in f:
        words = line.strip().split()
        # print(words)
        if words[0] == '$':
            if words[1] == 'cd':
                if words[2] == '/':
                    path = ['/']
                elif words[2] == '..':
                    path.pop()
                else:
                    path.append(words[2])
                # print(words, path)
        elif words[0].isnumeric():
            folderPath = path[0] + '/'.join(path[1:])
            # files.append(folderPath + '/' + words[1])
            folderPathSplits = folderPath.split('/')
            if len(folderPathSplits) >= 2:
                for i in range(len(folderPathSplits)):
                    subPath = '/'.join(folderPathSplits[0:i+1])
                    # print(subPath)
                    if subPath in sizes:
                        sizes[subPath] += int(words[0])
                    else:
                        # print('ERROR! Path ' + subPath + ' does NOT exist!')
                        sizes[subPath] = int(words[0])

# print(files)
# print(sizes)

totalFoldersSize = 0

for path, size in sizes.items():
    # print(path, size)
    if size <= 100000:
        totalFoldersSize += size

print(totalFoldersSize)

usedSpace = sizes['']
freeSpace = capacity - usedSpace
# print(freeSpace)
sortedSizes = {k: v for k, v in sorted(sizes.items(), key=lambda item: item[1])}
# print(sortedSizes)

for path, size in sortedSizes.items():
    # print(path, size)
    if freeSpace + size >= neededSpace:
        print(path, size)
        break
