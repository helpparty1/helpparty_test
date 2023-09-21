import sys #1,2,3,4,5
array={"c=":1,"c-":1,"dz=":1,"d-":1,"lj":1,"nj":1,"s=":1,"z=":1}
count=0
j=1
sentense=str(sys.stdin.readline().strip())
add_sentense=""

for i in array.keys():
    sentense=sentense.replace(i,str(j))

for j in sentense:
    if(j=="1"):
        count+=1
    else:
        count += 1

print(count)
