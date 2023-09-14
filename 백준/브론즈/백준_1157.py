import sys

array=[]
sentense=str(sys.stdin.readline()).upper().rstrip() #rstrip기억, #Mississipi #baaa
fake=list(set(sentense)) #중복 되는 단어를 뺌 #misp #ba
for i in fake:
    a=sentense.count(i)
    array.append(a) #1,4,1,4 #1,3

if(array.count(max(array))>1):
    print("?")
else:
    print(fake[array.index(max(array))])
