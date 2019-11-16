
import sys

#处理低级的
# for i in range(1,10,1):
#     sum += 2**i
#     if sum >=t:
#         result = i
#         break
# last_result = t - 2*(2**i -1)
# bin01 = bin(last_result-1)
# str_bin = str(bin01)[-result:]
# str_bin = str_bin.replace('0',alist[0])
# str_bin = str_bin.replace('1',alist[1])
# print(str_bin)

#思想：找出是几位数后，利用二进制数
def fun(alist):
    t = int(alist[2])
    count = 0
    while t>=2:
        t=t//2
        count +=1
    remain = int(alist[2]) - (2**count -2)
    str_1 = str(bin(remain-1)[-count:])
    result = str_1.replace('0',alist[0])
    result = result.replace('1',alist[1])
    return result

# alist = list(sys.stdin.readline().strip().split())
alist =['3','6','16']
print(fun(alist))
#方法三：最准确的
import math
#log 默认是e为底
def fun2(alist):
    t = int(alist[2])
    count = math.ceil(math.log(t/2+1,2))
    remain = int(alist[2]) - (2 ** count - 2)
    str_1 = str(bin(remain - 1).replace('b','0')[-count:])#考虑了bin（0）第一个的特殊情况
    result = str_1.replace('0', alist[0])
    result = result.replace('1', alist[1])
    return result
print(fun2(alist))