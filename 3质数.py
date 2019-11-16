
import sys

def zhishu(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                result = 'NO'
                break
            else:
                result = 'YES'
            return result
    else:
        result = 'NO'
        return result

n = int(sys.stdin.readline())
result = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().strip().split()))
    num = a[0]**2 - a[1]**2
    result.append(zhishu(num))
for i in result:
    print(i)