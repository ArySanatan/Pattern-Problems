"""
Pattern:
1 2 3 4 5 
  1 2 3 4
    1 2 3
      1 2
        1
        
        """

n=5

for i in range(n):
    h=1
    for j in range(i):
        print(" ",end=" ")
    
    for j in range(i,n):
        print(h,end=" ")
        h+=1
        
    print()