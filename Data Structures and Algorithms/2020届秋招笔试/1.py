import sys
n = list(map(int,sys.stdin.readline().strip().split(',')))
res = 0
if len(n)==0:
    print(0)
else:
    n1 = sorted(n)
    for i in range(len(n)):
        if n[i] != n1[i]:
            res+=1
    if res==0:
        print(0)
    else:
        print(res)