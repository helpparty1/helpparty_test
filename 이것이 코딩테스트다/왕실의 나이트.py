dir=input() #a1
row=int(dir[1]) #행
column=int(ord(dir[0]))-96 #열
count=8
choice=[(-2,-1),(-2,-1),(-1,-2),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
for i in choice:
    if(i[0]+row<=0 or i[0]+row>8):
        count-=1
    elif(i[1]+column<=0 or i[1]+row>8):
        count-=1

print(count)
#c3의 경우 경우의 수 게산
"""
b1 (-2,-1)
d1 (-2,1)
a2 (-1,-2)
e2 (-1,2)
a4 (1,-2)
b5 (2,-1)
c5 (2,1)
e2 (1,2)

"""