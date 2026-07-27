print("****LEAP YEAR****")
num1 = int(input("enter a year: "))
if num1 % 400 == 0 and num1 % 100 ==0:
    print(num1,"is leap year")
elif num1 % 4 == 0 and num1 % 10 != 0:
    print(num1, "is leap year")
else:
    print(num1, "not a leap year!")
