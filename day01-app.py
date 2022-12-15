calories = 0
maxCalories = 0
arrCalories = []

with open('day01-input.txt') as f:
    for line in f:
        if line == '\n':
            if calories > maxCalories:
                maxCalories = calories
            arrCalories.append(calories)
            calories = 0
        else:
            calories += int(line)

arrCalories.sort()

# print(arrCalories)
print(maxCalories)
print(sum(arrCalories[-3:]))
