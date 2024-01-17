def solution(answers):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]
    for i,j in enumerate(answers):
        if j==one[i%len(one)]:
            count[0]+=1
        if j==two[i%len(two)]:
            count[1]+=1
        if j==three[i%len(three)]:
            count[2]+=1    
    max_count=max(count)
    result=[]
    for k,l in enumerate(count):#enumerate
        if max_count==count[k]:
            result.append(k+1)
    return result