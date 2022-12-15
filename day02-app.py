score = 0

# with open('day02-input.txt') as f:
#     for line in f:
#         state = line.split()
#         match state[1]:
#             case 'X': # ROCK by me
#                 score += 1
#                 match state[0]:
#                     case 'A': # draw
#                         score += 3
#                     case 'C': # SCISSORS by opponent, I WIN
#                         score += 6
#             case 'Y': # PAPER by me
#                 score += 2
#                 match state[0]:
#                     case 'A': # ROCK by opponent, I WIN
#                         score += 6
#                     case 'B': # draw
#                         score += 3
#             case 'Z': # SCISSORS by me
#                 score += 3
#                 match state[0]:
#                     case 'B': # PAPER by opponent, I WIN
#                         score += 6
#                     case 'C': # draw
#                         score += 3

with open('day02-input.txt') as f:
    for line in f:
        state = line.split()
        match state[0]:
            case 'A': # ROCK by opponent
                match state[1]:
                    case 'X': # I LOOSE with SCISSORS
                        score += 0 + 3
                    case 'Y': # we DRAW with another ROCK
                        score += 3 + 1
                    case 'Z': # I WIN with PAPER
                        score += 6 + 2
            case 'B': # PAPER by opponent
                match state[1]:
                    case 'X': # I LOOSE with ROCK
                        score += 0 + 1
                    case 'Y': # we DRAW with another PAPER
                        score += 3 + 2
                    case 'Z': # I WIN with SCISSORS
                        score += 6 + 3
            case 'C': # SCISSORS by opponent
                match state[1]:
                    case 'X': # I LOOSE with PAPER
                        score += 0 + 2
                    case 'Y': # we DRAW with another SCISSORS
                        score += 3 + 3
                    case 'Z': # I WIN with ROCK
                        score += 6 + 1

print(score)
