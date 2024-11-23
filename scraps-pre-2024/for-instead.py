# listOfAvgs = []
# num = none
# for each in range(100):  
#     try:
#         num = int(input("Enter a number: "))
#         if num == 0 or num < 0:
#             num = int(input("Enter a different number: "))
#     except Exception as e:
#         print("Error", e)


avgs = []

def getNum():
    num = int(input("Enter a number: "))
    return num


def someProg():
    try:
        userInput = getNum()
        if userInput == "done":
            print(avgs)
        else:
            num = getNum()
            avgs.append(num)
            someProg()      
    except Exception as e:
        print("Error:", e)
        someProg()

    

someProg()