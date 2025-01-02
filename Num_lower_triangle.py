"""Pattern
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

#code
n=5

for i in range(n):
    h=5
    for j in range (i+1):
        print(h,end=" ")
        h=h-1
    
    print()