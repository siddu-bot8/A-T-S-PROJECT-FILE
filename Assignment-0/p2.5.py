print("****VOWEL OR CONSONANT****")
num1 = input("enter a character: ")
list1 = ["a","A","E","e","I","i","O","o","U","u"]
if num1 in list1:
    print(num1, "is vowel")
else:
    print(num1, "is consonant")