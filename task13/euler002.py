import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    a=0
    b=1
    c=0
    d=0

    while(c<n):
        if c%2==0:
            d+=c
        c=a+b
        a=b
        b=c
    print (d)
