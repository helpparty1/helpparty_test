import sys

X = int(sys.stdin.readline().strip())  # 입력에서 개행 문자를 제거하여 정수로 변환
stick = [64, 32, 16, 8, 4, 2, 1]
i = 0
count = 0

while(1):
    if X == 0:
        break
    elif stick[i] <= X:
        X -= stick[i]
        count += 1
    i += 1

print(count)
