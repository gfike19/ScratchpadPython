import string

punc = string.punctuation

msg = input("Enter some text: ")

alist = []

newMsg = ""

for each in msg:
    if each.isalpha():
        temp = ord(each)
        newMsg += "{0:b}".format(temp)
        newMsg += " "
    elif each in punc or each == " ":
        newMsg += each
    # else:
    #     alist.append(each)



# for each in alist:
#     if type(each) == int:
        
#     else:
#         newMsg += each

print(newMsg)