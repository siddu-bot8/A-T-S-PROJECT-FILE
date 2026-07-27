ch = 65

for i in range(5):              # rows
    for j in range(i + 1):      # columns
        print(chr(ch), end=" ")
    ch += 1
    print()



# A 
# B B       
# C C C     
# D D D D   
# E E E E E 