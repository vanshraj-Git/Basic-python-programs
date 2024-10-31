# Compact diamond
#     1 
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1
n=5
a=5
for i in range (1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for j in range (1,i+1):
        print(i,"",end="")
    print()
for i in range (1,n):
    a-=1
    for j in range(0,i):
        print(" ",end="")
    for j in range(i,n):
        print(a,"",end="")
    print()