import sys
from math import *

array=[]
sum=0
room=str(sys.stdin.readline().strip()) #9999
real=list(set(room)) #9

for i in real: #6969
    if i=='6' or i=='9':
        sum+=room.count(i)

    else:
     array.append(room.count(i)) #2
sum=ceil(sum/2) #2

if(len(array)==0):
    print(sum)
elif(max(array)>=sum):
    print(max(array))
else:
    print(sum)
