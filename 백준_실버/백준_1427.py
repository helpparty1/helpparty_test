import sys #1,2,2,3,3,3,4,4,4,4,5,5,5,5,5 배열 짜보기r
N=str(sys.stdin.readline().strip())
array=[]
sentense=""

for i in range(0,len(N),1):
    array.append(N[i])

array.sort()
array.reverse()


for j in range(0,len(array),1):
    sentense=sentense+str(array[j])

print(int(sentense))
