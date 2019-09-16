import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    s=0
    for i in range(n): 
        
        if i%3==0 or i%5==0:
    
            s+=i
            i=i//2
        
    print (s)
