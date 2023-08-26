import sys

month,day=map(int,sys.stdin.readline().split()) #2월 26일

array=[31,28,31,30,31,30,31,31,30,31,30,31]
mon=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


sum=sum(array[0:month]) #총 날짜 게산
sum=sum-(array[month-1]-day)-1
sum=sum%7
print(mon[sum])