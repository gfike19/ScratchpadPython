import string

repeat = "y"
allChars = string.ascii_lowercase
hw  = open("hw.txt", "a+")
while repeat == "y":
    plain = input("Enter message to encrypt: ")
    encrypt = ""
    k = int(input("Enter multiplier: "))

    for each in plain:
        if (each.isalpha()):
            x = allChars.find(each)
            hw.write(str(x) + "\t")
            y = (k * x) % 26
            hw.write(str(y) + "\t")
            newChar = allChars[y]
            hw.write(newChar + "\t")
            encrypt += newChar
        else:
            hw.write(each)
        hw.write("\n")
    
    print("Encrypted message is:", encrypt)
    repeat = input("Repeat (y/n)? ")
hw.close()
