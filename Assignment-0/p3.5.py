print("****FACTORIAL OF A NUMBER****")
m = int(input("enter a number: "))
i=0
n = 1
while i < m:
    n = n * (m-i)
    i = i+1
print("Factorial of",m, "is: ",n)