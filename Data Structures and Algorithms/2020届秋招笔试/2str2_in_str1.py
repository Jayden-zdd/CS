import sys
# str1 = sys.stdin.readline().strip()
# str2 = sys.stdin.readline().strip()
str1 = 'eeaaccebce'
str2 = 'abc'
def fun(str1,str2):
    origin_str1 = str1
    if str1 and str2=='':
        result = origin_str1
        return result
    index = []
    count = 0
    for i in range(len(str2)):
        item = str2[i]
        item_index = str1.find(item)
        if item_index == -1:
            result = "\"\""
            return result
        if count ==0:
            index.append(item_index)
        else:
            index.append(item_index+count)
        str1 = str1[:item_index]+str1[item_index+1:]
        count +=1
    result = origin_str1[min(index):max(index)+1]
    return result
print(fun(str1,str2))
