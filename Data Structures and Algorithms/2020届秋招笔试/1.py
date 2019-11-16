import sys
n = int(sys.stdin.readline())
alist = list(map(int,sys.stdin.readline().strip().split()))
sum = 0
for i in alist:
    sum += 1.0/i
print("%.2f"%sum)