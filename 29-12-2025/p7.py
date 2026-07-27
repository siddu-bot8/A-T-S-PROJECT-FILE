n = 5
for i in range(n):   # i = 4, 3, 2, 1
    for j in range(2*i):  # spaces
        print(end=" ")
    for k in range(5-i):      # stars
        print("*", end=" ")
    print()




# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *