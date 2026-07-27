# ch = 97

# for i in range(5):              # rows
#     for j in range(i + 1):      # columns
#         print(chr(ch), end=" ")
#         ch += 1
#     print()




# a 
# b c 
# d e f
# g h i j
# k l m n o


# class surya:
#     a =10
#     def b():
#         return "ok"
    
# s = surya()
# # s.a()
# print(surya.a)
# print(surya.b())
# print(s.a)
# print(s.b())


class surya:
    def __init__(self, name , color , model):
        self.name1 = name 
        self.color1 = color
        self.model1 = model


s = surya("bmw","white","m4")
print(s.name1)
surya()