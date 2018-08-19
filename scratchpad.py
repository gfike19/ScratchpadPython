# import random

# poem = open("poem.txt")

# aList = []

# for line in poem:
#     aList.append(line)

# poem.close()

# dit = {}

# i = 0

# while i < 10:
#     for line in aList:
#         key = random.choice(line)
#         val = random.randint(0, 100)
#         val2 = random.randint(0, 100)
#         tup = (val, val2)
#         dit[key] = tup
#     i += 1

import random

dic = {'g': (40, 69), 'h': (100, 40), 'W': (27, 95), 's': (5, 77), '\n': (63, 33), ' '
: (59, 17), 'i': (26, 39), 'p': (7, 81), 'a': (8, 64), 'l': (38, 50), 'r': (86,35), 't': (34, 27), 'd': (63, 9), ':': (3, 38), 'e': (82, 36), 'o': (100, 12), 'm': (79, 60), 'T': (27, 59), 'f': (14, 77), '?': (21, 96), 'A': (37, 44), 'n': (
80, 84), 'D': (47, 62), 'w': (40, 61), 'u': (20, 75), 'I': (77, 57), 'v': (87, 17), 'b': (25, 39), '.': (99, 94), 'y': (36, 49), 'z': (48, 30), "x": (84, 43), "w": (37, 15), ',': (51, 61)}

listOfValues = []

for k,v in dic.items():
    listOfValues.append(v)

print(listOfValues)

for tup in listOfValues:
    print(tup[0], tup[1])