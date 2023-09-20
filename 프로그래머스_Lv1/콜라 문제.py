def solution(a, b, n):
    """
    총:20병, 6병
    총:8병,  2병
    총:4병,  1병
    """
    solution=0
    sum=0

    while(1):
        solution=solution+((n//a)*b)
        n=(n//a)*b+(n%a)


        if(a>n):
            break


    return solution
