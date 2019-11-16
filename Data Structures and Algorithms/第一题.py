import sys
# n = int(sys.stdin.readline())
# alist = []
# for i in range(n):
# 	alist.append(list(map(int,sys.stdin.readline().strip().split())))
n = 2
alist = [[2, 1], [30, 2]]
alist = sorted(alist,key=lambda x:x[1], reverse=True)
l=0
#完成
v =0
for i in alist:
    l = l + (v*i[1] + 0.5 * i[0] * (i[1]**2))
    v = v + i[0] * i[1]
print("%.2f"%l)#121.00
print('{:.2f}'.format(l))#121.00
print(round(l,3))#121.0