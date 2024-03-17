import random

input("do you want to roll a dice?")

response="y"
while response=="y":
    num=random.randint(1,6)
    if num==1:
        print("The value is 1")
    if num==2:
        print("The value is 2")
    if num==3:
        print("The value is 3")
    if num==4:
        print("The value is 4")
    if num==5:
        print("The value is 5")
    if num==6:
        print("The value is 6")
    response=input("press y to roll again and n to exit")
    print("\n")
