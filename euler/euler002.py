import sys


t = int(input().strip())
for a0 in range(t):
    exceed = int(input().strip())
    a,b = 1,1
    summ = 0
    while(True):
       a = a + b
       b = a + b
       if a < exceed and a%2==0:
           summ+=a
       if b<exceed and b%2==0:
           summ+=b
       if a >= exceed:
           break
    print(summ)