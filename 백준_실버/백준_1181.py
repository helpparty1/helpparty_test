import sys ###어쩌다 보니 하드 코딩.... 실력에는 도움이 되겠지
N=int(sys.stdin.readline().strip())
array=[]

for i in range(N):
    sentense=str(sys.stdin.readline().strip())
    array.append(sentense)

array=list(set(array))
array.sort()
array.sort(key=len)
for j in array:
    print(j)
