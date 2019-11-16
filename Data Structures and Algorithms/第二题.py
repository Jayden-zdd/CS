import sys
# first_line = sys.stdin.readline().strip().split()
# n = int(first_line[0])
# m = int(first_line[1])
# second_line = sys.stdin.readline().strip().split()
# alist = [int(i) for i in second_line]
max_num = 0
n = 10
m = 6
alist = [6,4,2,10,3,8,5,9,4,1]
for i in range(n-m+1):
    total = sum(alist[i:i+m])
    #自己蠢写的
    # total = 0
    # for j in range(i,i+m):
    #     total += alist[j]
    if total > max_num:
        max_num = total
result = max_num/(m*1.0)
print('%.3f'%result)

#第二种方法：
v = 0
_sum = [v for i in range(n)]
print(_sum)
_sum[0] = alist[0]
print(_sum)
for i in range(1,n):
    _sum[i] = alist[i] + _sum[i-1]
    print(_sum)
max_sum = _sum[m-1]
print(max_sum)
for i in range(n-m):
    temp = _sum[i+m] - _sum[i]
    max_sum = max(max_sum,temp)
print('{:.3f}'.format(max_sum/m))

