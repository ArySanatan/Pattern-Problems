n=5

for i in range(n):
    h=1
    for j in range(i):
        print(" ",end=" ")
    
    for j in range(i,n):
        print(h,end=" ")
        h+=1
        
    print()