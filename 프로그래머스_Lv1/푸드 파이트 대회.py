def solution(food): #0,1,1,1,2,2,2,2,3,3,3,3,3,3
    answer = '0'
    new='0'
    del food[0]
    for i,j in enumerate(food): #i=0,j=3 / i=1,j=4
        if(j%2==0):
            N=j//2 #N=1 / N=2
            answer=(str(i+1)*N)+answer
            answer=answer+(str(i+1)*N)
        
        else:
            N=j//2 #N=1
            answer=(str(i+1)*N)+answer #answer='01'
            answer=answer+(str(i+1)*N) #answer='101'
    a=answer.find('0')
    b=answer[a+1:]
    new=b+new
    b=b[::-1]
    new=new+b
    return new
