print("****VOWELS IN A STRING****")
num1 = input("Enter a word: ")
list1 = ["a","A","E","e","I","i","O","o","U","u"]
count=0
for i in num1:
    if i in list1:
        count +=1
print("ouput:",count)