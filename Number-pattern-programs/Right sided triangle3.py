#   1 1 1 1 1 
#     2 2 2 2
#       3 3 3
#         4 4
#           5

n=5
for i in range(1,n+1):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,n+1):
        print(i,"",end="")
    print()