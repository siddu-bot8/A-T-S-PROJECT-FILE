print("****TEMPERATURE CHECK****")
num1 = float(input("enter a temperature: "))
if num1<15:
    print("Cold")
elif num1>15 and num1<30:
    print("Moderate")
else:
    print("Hot")
