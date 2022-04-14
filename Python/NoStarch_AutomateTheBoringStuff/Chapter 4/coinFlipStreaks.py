import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(100):
        results.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(results)):
        slice = (results[i:i+6])
        sliceSum = sum((results[i:i+6]))
        if len(slice) < 6:
            break
        if sliceSum == 0 or sliceSum == 6:
            numberOfStreaks += 1

print('Number of streaks: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

#Something is wrong here, 293.31% does not seem correct...