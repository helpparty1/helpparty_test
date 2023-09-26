import sys
X=int(sys.stdin.readline().strip()) #1,2,3,4,5,6,7,8,9,10 55
i=1
while(1):
    X=X-i
    if X<=i:
        break
    i+=1
print(i)
