import sys

ss = sys.stdin.readline()
adict = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}#数字
bdict = {0:'零', 1:'十',2:'百',3:'千',4:'万',5:'十',6:'百'}#单位
try:
    ss = int(ss)
except:
    print('输入错误')

def turn(x,y):
    if y>=1:
        a = int(x)//pow(10,y)
        b = int(x)%pow(10,y)
        c = adict[str(a)] + bdict[y]
        if y>4 and b<pow(10,y):#处理大于十万的数字
            c+=bdict[4]
        if (len(str(x))-len(str(b))) >=2 and b!=0:
            c+=bdict[0]
    else:
        a = x
        b = 0
        c = adict[str(a)]
    return (c,b,)

def int_chinese(x):
    c = turn(x, len(str(x))-1)
    a = c[0]
    b = c[1]
    while b!=0:
        a += turn(b, len(str(b))-1)[0]
        b = turn(b, len(str(b))-1)[1]
    return a

print(int_chinese(ss))