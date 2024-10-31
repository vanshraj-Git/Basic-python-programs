# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

n=10
for i in range(0,n+1,2):
    for j in range(1,i+1,2):
        print(j,end=" ")
    print()