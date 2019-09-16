import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())


    x=1

    for i in range(1,n+1):
        x=(x*i) // (math.gcd(x,i))

    print (x)
