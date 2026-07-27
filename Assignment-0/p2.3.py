print("****CHECK DIVISIBLE BY 2 AND 3 OR BOTH****")
num1 = int(input("enter a number: "))
if  num1 % 2==0:
    print(num1,"is divisible with 2", end =" ")
if  num1 % 3 == 0:
    print(",3", end=" ")
if  num1 % 2 ==0 and num1 % 3 ==0:
    print("and with both also")
