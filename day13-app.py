with open('day13-input-test.txt') as f:
    left = None
    right = None
    for line in f:
        # print(line.strip())
        if left == None:
            left = eval(line.strip())
        elif right == None:
            right = eval(line.strip())
        else:
            print(left, right)
            left = None
            right = None
