array=[]

for i in range(9):
    nan=int(input()) #20 7 23 19 10 15 25 8 13
    array.append(nan)

array.sort()
num=sum(array)-100 #num=40
a=0
b=0

for j in range(0,8,1): #j=4,k=5 j=7k=8
    for k in range(j+1,9,1):
        if(array[j]+array[k]==num):
            a=array[j]
            b=array[k]

array.remove(a)
array.remove(b)
for t in range(0,7,1):
    print(array[t])

