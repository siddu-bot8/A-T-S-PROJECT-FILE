print("****LARGEST OF 3****")
num1 = int(input("enter a number: "))
num2 = int(input("enter b number: "))
num3 = int(input("enter c number: "))
if num1 < num2 and num1 < num3:
    print(num1,"is smaller than", num2 ,"and", num3)
elif num2 < num3:
    print(num2,"is smaller than", num1 ,"and", num3)
else:
    print(num3,"is smaller than", num1 ,"and" , num2)
