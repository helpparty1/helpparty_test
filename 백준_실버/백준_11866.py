import sys
from collections import deque
#1,4,
N,M=map(int,sys.stdin.readline().split())
array=deque()
array2=[]
for i in range(1,N+1,1):
    array.append(i)

#array 1,2,3,4,5,6,7
for i in range(1,N+1,1):
    for j in range(M-1):
        A=array.popleft()
        array.append(A)
    B=array.popleft()
    array2.append(B)
print("<", ", ".join(list(map(str,array2))), ">",sep="")