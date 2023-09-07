import sys

A,B=map(int,sys.stdin.readline().split()) #A=24,B=16
a,b=A,B #a=24 b=16
while(b!=0):
    a=a%b #a=8 a=0
    a,b=b,a #a=16 b=8 / a=8, b=0

print(a)ㄴ
print(A*B//a)