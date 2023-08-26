while(1):
    n = str(input())

    if(n=='0' or n[0]=='0'):
        break

    elif(n==n[::-1]):
        print("yes")

    elif(n!=n[::-1]):
        print("no")