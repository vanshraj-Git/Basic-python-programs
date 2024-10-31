# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1

n=5
p=5
for i in range(0,n):
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print()
    