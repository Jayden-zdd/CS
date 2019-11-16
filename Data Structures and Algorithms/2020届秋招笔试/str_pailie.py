
def func(ss):
    res = []
    if len(ss)<=1:
        return ss
    for i in range(len(ss)):
        ss_list = list(map(lambda x:ss[i]+x, func(ss[:i]+ss[i+1:])))
        for item in ss_list:
            if item not in res:
                res.append(item)
    return res

a = ['1','2','1']
a = list(a)
result = func(a)
n =3
for i in result:
    out = []
    for j in range(n-1):
        print(i[j]+ ' ',end='')
    print(i[n-1])
