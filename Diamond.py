
n=5

for i in range(4):
    for j in range(i,5):
        print(" ",end=" ")
    
    for j in range(i+1):
        print("*",end=" ")
    
    for j in range(i):
        print("*",end=" ")
    
    print()

for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    
    for j in range(i,5):
        print("*",end=" ")
    for j in range(i,4):
        print("*",end=" ")
    
    print()