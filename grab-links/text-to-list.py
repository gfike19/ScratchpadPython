newFile = open("linkList.py", "w")
oldFile = open("all-list-items.txt", "r")

newFile.write("all_links = [")

for line in oldFile:
    newFile.write(line + ",")
oldFile.close()
newFile.write("]")
newFile.close()