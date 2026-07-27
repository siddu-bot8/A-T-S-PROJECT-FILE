print("**** SUM OF ALL NUMBERS ARE DIVISIBLE BY 3****")
count = 0
for i in range(1,101):
    if i%3==0:
        count = count+i

print(count)