import sys
test=int(input()) #test=3
data=list(map(int,sys.stdin.readline().split())) #data=40,50,60
new_data=[]
max=max(data) #max=60

for i in range(0,test,1):
    new=data[i]/max*100
    new_data.append(new)

print(sum(new_data)/test)