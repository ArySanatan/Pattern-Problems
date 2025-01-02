"""
Pattern:
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *               """
          
n=5

for i in range(n-1):
    for j in range(i,5):
        print(" ",end=" ")
    
    for j in range(i+1):
        print("*",end=" ")
    
    for j in range(i):
        print("*",end=" ")
    
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    
    for j in range(i,5):
        print("*",end=" ")
    for j in range(i,4):
        print("*",end=" ")
    
    print()