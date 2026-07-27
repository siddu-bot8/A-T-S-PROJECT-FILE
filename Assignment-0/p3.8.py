print("****REVERSING A NUMBER****")
num1 = int(input("Enter a numbers: "))
rev = 0
while num1>0:
    n = num1%10
    rev = rev*10 + n
    num1 = num1//10
print("Reverse of give number: ",rev)
