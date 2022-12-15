# containedAssignments = 0

# with open('day04-input.txt') as f:
#     for line in f:
#         sections = line.strip().split(',')
#         left = sections[0].split('-')
#         right = sections[1].split('-')
#         leftLo = int(left[0])
#         leftHi = int(left[1])
#         rightLo = int(right[0])
#         rightHi = int(right[1])
#         # print(leftLo, leftHi, rightLo, rightHi)
#         if leftLo <= rightLo and leftHi >= rightHi:
#             containedAssignments += 1
#         elif leftLo >= rightLo and leftHi <= rightHi:
#             containedAssignments += 1

# print(containedAssignments)

overlappingAssignments = 0

with open('day04-input.txt') as f:
    for line in f:
        sections = line.strip().split(',')
        left = sections[0].split('-')
        right = sections[1].split('-')
        leftLo = int(left[0])
        leftHi = int(left[1])
        rightLo = int(right[0])
        rightHi = int(right[1])
        # print(leftLo, leftHi, rightLo, rightHi)
        if leftLo <= rightLo and leftHi >= rightHi:
            overlappingAssignments += 1
        elif leftLo >= rightLo and leftHi <= rightHi:
            overlappingAssignments += 1
        elif leftHi >= rightLo and leftLo <= rightHi:
            overlappingAssignments += 1
        elif rightHi >= leftLo and rightLo <= leftHi:
            overlappingAssignments += 1

print(overlappingAssignments)

