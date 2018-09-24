import string

letters = string.ascii_lowercase

i = 0

dit = {}

for each in letters:
    dit[each] = i
    i += 1

pos = int(input("Enter a number: "))

for k, v in dit.items():
    if v == pos:
        print(k)