import sys
N=int(input())
array=[]
for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
for j in array:
    print(j)
