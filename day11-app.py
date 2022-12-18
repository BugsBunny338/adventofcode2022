import time

start = time.time()

# monkeys = [{
#     'items': [79, 98],
#     # 'operation': lambda x: (x * 19),
#     'operation': lambda x: (x * 19) % (23 * 19 * 13 * 17),
#     'nextMonkey': lambda x: 2 if x % 23 == 0 else 3,
#     'inspectedItems': 0
# }, {
#     'items': [54, 65, 75, 74],
#     # 'operation': lambda x: (x + 6),
#     'operation': lambda x: (x + 6) % (23 * 19 * 13 * 17),
#     'nextMonkey': lambda x: 2 if x % 19 == 0 else 0,
#     'inspectedItems': 0
# }, {
#     'items': [79, 60, 97],
#     # 'operation': lambda x: (x * x),
#     'operation': lambda x: (x * x) % (23 * 19 * 13 * 17),
#     'nextMonkey': lambda x: 1 if x % 13 == 0 else 3,
#     'inspectedItems': 0
# }, {
#     'items': [74],
#     # 'operation': lambda x: (x + 3),
#     'operation': lambda x: (x + 3) % (23 * 19 * 13 * 17),
#     'nextMonkey': lambda x: 0 if x % 17 == 0 else 1,
#     'inspectedItems': 0
# }]

monkeys = [{
    'items': [89, 73, 66, 57, 64, 80],
    # 'operation': lambda x: x * 3,
    'operation': lambda x: (x * 3) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 6 if x % 13 == 0 else 2,
    'inspectedItems': 0
}, {
    'items': [83, 78, 81, 55, 81, 59, 69],
    # 'operation': lambda x: x + 1,
    'operation': lambda x: (x + 1) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 7 if x % 3 == 0 else 4,
    'inspectedItems': 0
}, {
    'items': [76, 91, 58, 85],
    # 'operation': lambda x: x * 13,
    'operation': lambda x: (x * 13) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 1 if x % 7 == 0 else 4,
    'inspectedItems': 0
}, {
    'items': [71, 72, 74, 76, 68],
    # 'operation': lambda x: x * x,
    'operation': lambda x: (x * x) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 6 if x % 2 == 0 else 0,
    'inspectedItems': 0
}, {
    'items': [98, 85, 84],
    # 'operation': lambda x: x + 7,
    'operation': lambda x: (x + 7) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 5 if x % 19 == 0 else 7,
    'inspectedItems': 0
}, {
    'items': [78],
    # 'operation': lambda x: x + 8,
    'operation': lambda x: (x + 8) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 3 if x % 5 == 0 else 0,
    'inspectedItems': 0
}, {
    'items': [86, 70, 60, 88, 88, 78, 74, 83],
    # 'operation': lambda x: x + 4,
    'operation': lambda x: (x + 4) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 1 if x % 11 == 0 else 2,
    'inspectedItems': 0
}, {
    'items': [81, 58],
    # 'operation': lambda x: x + 5,
    'operation': lambda x: (x + 5) % (13 * 3 * 7 * 2 * 19 * 5 * 11 * 17),
    'nextMonkey': lambda x: 3 if x % 17 == 0 else 5,
    'inspectedItems': 0
}]

rounds = 10000

while rounds > 0:
    for monkey in monkeys:
        while len(monkey['items']):
            item = monkey['items'].pop(0)
            worryLevel = int(monkey['operation'](item)) # used to be / 3 in Part One
            nextMonkey = monkey['nextMonkey'](worryLevel)
            monkeys[nextMonkey]['items'].append(worryLevel)
            monkey['inspectedItems'] = monkey['inspectedItems'] + 1
            # print(item, worryLevel, nextMonkey, monkey['inspectedItems'])
    rounds = rounds - 1
    # if rounds % 50 == 0:
    #     print(f'ROUND: {rounds}')

# print(monkeys[0]['items'])
# print(monkeys[1]['items'])
# print(monkeys[2]['items'])
# print(monkeys[3]['items'])

print(monkeys[0]['inspectedItems'])
print(monkeys[1]['inspectedItems'])
print(monkeys[2]['inspectedItems'])
print(monkeys[3]['inspectedItems'])
print(monkeys[4]['inspectedItems'])
print(monkeys[5]['inspectedItems'])
print(monkeys[6]['inspectedItems'])
print(monkeys[7]['inspectedItems'])

print(f'duration: {time.time() - start}')
