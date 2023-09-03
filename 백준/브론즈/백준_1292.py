import sys
A,B=map(int,sys.stdin.readline().split())
array=[]

for i in range(1000): #i=1 #i=2
    for j in range(i): #j=1 #j=2
        array.append(i)

print(sum(array[A-1:B]))