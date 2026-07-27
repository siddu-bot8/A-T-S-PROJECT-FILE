print("****FORM A TRIANGLE****")
num1 = int(input("enter a side: "))
num2 = int(input("enter b side: "))
num3 = int(input("enter c side: "))
if (num1 + num2 > num3) and (num2 + num3 > num1) and num3 + num1 > num2:
    print("Can form a triangle")
else:
    print("Cant form a triangle!")