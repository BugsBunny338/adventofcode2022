quad = []

with open('day06-input.txt') as f:
    for line in f:
        for idx, ch in enumerate(line):
            if len(quad) >= 14:
                quad.pop(0)
            quad.append(ch)
            if len(quad) == 14 and len(set(quad)) == 14:
                print(idx + 1)
                break
