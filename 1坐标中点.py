import sys
# a = list(map(int,sys.stdin.readline().strip().split()))
a = input()
print(a)
a = list(map(int,a.split()))
print(a)
result = str((a[0] + a[2])//2) +' '+ str((a[1] + a[3])//2)
print(result)