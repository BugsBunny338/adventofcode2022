columns = [
    ['Z', 'P', 'M', 'H', 'R'],
    ['P', 'C', 'J', 'B'],
    ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
    ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
    ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
    ['T', 'F', 'S', 'Z', 'B', 'G'],
    ['N', 'R', 'V'],
    ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
    ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
]

# with open('day05-input.txt') as f:
#     for line in f:
#         if line.startswith('move'):
#             words = line.strip().split()
#             cnt = int(words[1])
#             frm = int(words[3])
#             too = int(words[5])
#             # print(cnt, frm, too)
#             for i in range(cnt):
#                 columns[too - 1].append(columns[frm - 1].pop())

# state = ''
# for column in columns:
#     state += column[-1]

# print(state)

with open('day05-input.txt') as f:
    for line in f:
        if line.startswith('move'):
            words = line.strip().split()
            cnt = int(words[1])
            frm = int(words[3])
            too = int(words[5])
            # print(cnt, frm, too)
            toBeMoved = []
            for i in range(cnt):
                toBeMoved.append(columns[frm - 1].pop())
            toBeMoved.reverse()
            columns[too - 1].extend(toBeMoved)

state = ''
for column in columns:
    state += column[-1]

print(state)
