import sys

def factorial(x):
    remember=1
    for i in range(x,1,-1):
        remember*=i

    return remember

N,K=map(int,sys.stdin.readline().split())
print(factorial(N)//(factorial(N-K) * factorial(K)))
