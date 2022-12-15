from itertools import islice

priorities = 0

# with open('day03-input.txt') as f:
#     for line in f:
#         left = line[:len(line) // 2]
#         right = line[len(line) // 2:]
#         common = ''.join(set(left).intersection(right))
#         priority = ord(common)
#         if priority >= 97 and priority <= 122:
#             priorities += priority - 96
#         else:
#             priorities += priority - 38

# print(ord('a'), ord('z'))
# print(ord('A'), ord('Z'))

with open('day03-input.txt') as f:
    allLines = [line.strip() for line in f]
    lines = []
    while (len(allLines)):
        for i in range(3):
            lines.append(allLines.pop())
        commonTmp = ''.join(set(lines[0]).intersection(lines[1]))
        common = ''.join(set(commonTmp).intersection(lines[2]))
        priority = ord(common)
        if priority >= 97 and priority <= 122:
            priorities += priority - 96
        else:
            priorities += priority - 38
        lines = []

print(priorities)
