print("****FIBONACCI SERIES****")
num1 = int(input("Enter how many terms: "))

a, b = 0, 1   # first two terms
i = 0

while i < num1:
    print(a, end=" ")   
    a, b = b, a + b    
    i += 1            
#didnt understand