import sys
A,B=map(int,sys.stdin.readline().split())
C=list(map(int,sys.stdin.readline().split()))
D=list(map(int,sys.stdin.readline().split()))
E=[]
E=C+D
count_len=len(E) #8개
E=list(set(E)) #6개
count_len=count_len-len(E)
print(A-count_len+B-count_len)

