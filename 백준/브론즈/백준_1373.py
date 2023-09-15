import sys ###어쩌다 보니 하드 코딩.... 실력에는 도움이 되겠지

N=str(sys.stdin.readline().strip())
count=0
answer=0
array=list(N)
array.reverse()
array2=[]


for i in array:
    if(count==0):
        answer+=int(i)*1 #1
    elif(count==1):
        answer += int(i) * 2  # 1
    elif(count == 2):
        answer += int(i) * 4  # 1
        count=-1
        array2.append(answer)
        answer=0
    count += 1

array2.append(answer)
array2.reverse()
result = ''.join(map(str,array2))
print(int(result))
#0011011
