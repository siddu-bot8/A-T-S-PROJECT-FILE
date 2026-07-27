print("**** PRIME NUMBERS BETWEEN 1 TO 50 ****")

for i in range(2, 51):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")


#didnt get