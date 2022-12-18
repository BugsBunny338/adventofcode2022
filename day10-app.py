x = [1]
signalStrengths = []
crt = []

def printStatus(i):
    print(f"during {i}th cycle: {x[i - 1]}")

def setSignalStrength(i):
    signalStrengths.append(i * x[i - 1])

def renderCrt():
    print(''.join(crt[0:40]))
    print(''.join(crt[40:80]))
    print(''.join(crt[80:120]))
    print(''.join(crt[120:160]))
    print(''.join(crt[160:200]))
    print(''.join(crt[200:240]))

with open('day10-input.txt') as f:
    for line in f:
        words = line.strip().split()
        # print(words)
        instruction = words[0]
        match instruction:
            case 'noop':
                # print(instruction)
                x.append(x[-1])
            case 'addx':
                value = int(words[1])
                # print(instruction, value)
                x.append(x[-1])
                x.append(x[-1] + value)

for i, v in enumerate(x):
    # printStatus(i)
    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
        # printStatus(i)
        setSignalStrength(i)
    if abs(i%40 - v) <= 1:
        crt.append('#')
    else:
        crt.append('.')

# print(len(x))
# print(signalStrengths)
print(sum(signalStrengths))
renderCrt()
