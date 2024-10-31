# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


n=5
p=1
for i in range(0,n):
    for j in range(0,i+1):
        print(p,end=" ")
    p+=1
    print()