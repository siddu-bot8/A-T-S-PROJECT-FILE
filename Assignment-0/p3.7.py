print("****NUMBER OF NUMBERS IN A NUMBER****")
num1 = int(input("Enter a numbers: "))
num2 = 0
while num1 > 0:          
    num1 = num1 // 10  
    num2 += 1          

print("Number of digits:", num2)
