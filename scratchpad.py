import random

poem = open("poem.txt")

aList = []

for line in poem:
    aList.append(line)

poem.close()

dit = {}

i = 0

while i < 10:
    for line in aList:
        key = random.choice(line)
        val = random.randint(0, 100)
        val2 = random.randint(0, 100)
        tup = (val, val2)
        dit[key] = tup
    i += 1

print(dit)