string = "Sphinx of black quartz, judge my vow!"
dit = {}

for each in string:
    if each not in dit:
        dit[each] = 1
    else:
        val = dit[each]
        dit[each] = val + 1

for k,v in dit.items():
    if v > 1:
        print(k)