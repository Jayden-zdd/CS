import sys
A = [None for i in range(0, 10)]
V = [False for i in range(0, 10)]
print(A,V)
N = int(sys.stdin.readline())
def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def dfs(cur):
    if cur == N:
        if is_prime(A[0]+A[N-1]):
            result.append(A[:N])
    else:
        for i in range(1, N+1):
            if not V[i]:
                if cur == 0 or is_prime(i+A[cur-1]):
                    V[i] = True
                    A[cur] = i
                    dfs(cur+1)
                    V[i] = False
result = []
dfs(0)
for item in result:
    if item[0]==1:
        print(' '.join(str(i) for i in item))
