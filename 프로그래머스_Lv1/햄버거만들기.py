def solution(ingredient):
    array=[]
    count=0
    
    for i in ingredient:
        array.append(i)
        if array[-4:]==[1,2,3,1]:
            count+=1
            for j in range(4):
                array.pop()
                
    return count