#   1                 1 
#   2 2             2 2
#   3 3 3         3 3 3
#   4 4 4 4     4 4 4 4
#   5 5 5 5 5 5 5 5 5 5
#   4 4 4 4     4 4 4 4
#   3 3 3         3 3 3
#   2 2             2 2 
#   1                 1

n=5
a=5
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1,end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()
for i in range(1,n):
    a-=1
    for j in range(i,n):
        print(a,end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,n):
        print(a,end=" ")
    print()