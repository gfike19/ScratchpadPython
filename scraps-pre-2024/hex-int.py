color = "#5DBCD2"
color = color[1:]
print(color)
lst = []
lst.append(color[0:2])
lst.append(color[2:4])
lst.append(color[4:6])
print(lst)
rgb = (int(lst[0],16), int(lst[1],16), int(lst[2],16))
print(rgb)