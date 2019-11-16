alist = [1,2,3,3,5,3]
dict = {0: [1, 2, 1], 1: [2, 4, 5], 2: [3, 6, 3]}
# import sys
# n = int(sys.stdin.readline())
# alist = list(map(int, sys.stdin.readline().strip().split()))
# q = int(sys.stdin.readline())
# dict = {}
# for i in range(q):
# 	dict[i] = list(map(int, sys.stdin.readline().strip().split()))
# # print(dict)
result = []
for values in dict.values():
    # print(values)
    # print(alist[values[0]-1:values[1]])
    result.append(alist[values[0]-1:values[1]].count(values[2]))
print(result)