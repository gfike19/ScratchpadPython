def getBinMsg(msg):
    lst = []
    for char in msg:
        lst.append(ord(char))

    msg = ""
    for each in lst:
        msg += "{0:b}".format(each)

    return msg 

repeat = 'y'

while repeat =='y':
    string = input("Enter a message: ")
    binMsg = getBinMsg(string)
    print("The binary version of", string, "is", binMsg)
    repeat = input("Enter another message? (y/n) ")