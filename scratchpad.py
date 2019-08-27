string = "Sphinx of black quartz, judge my vow!"
dit = {}

for each in string:
    if dit[each] == "":
        dit[each] = 1
    else:
        val = dit[each]
        dit[each] = val + 1

for k,v in dit:
    print(k + ": " + v)