number = int(input())  # 26
count = 0
remember = number

while (1):
    front = number // 10  # front=2 front=6
    back = number % 10  # back=6 back=8
    sum = front + back  # sum=8 sum=14
    if (sum < 10):
        number = back * 10 + sum  # back=68
        count += 1
        if (number == remember):
            break

    else:
        number = back * 10 + sum % 10
        count += 1
        if (number == remember):
            break

print(count)

# 2+6 = 8이다. 6+8 = 14이다. 8+4 = 12이다. 4+2 = 6