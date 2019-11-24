a_list = [1,2,3,4,5,6]
a_list = [i*2 for i in a_list]
print("a_list=",a_list)

a_dict = {1:[1,2,3,4,5,6],2:[2,3,4,5,6,7]}
for key,value in a_dict.items():
    print(id(value))
    if key ==1:
        value = [i * 2 for i in value]
        print(id(value))
    else:
        pass
        print(id(value))
#a_dict={1: [1, 2, 3, 4, 5, 6], 2: [2, 3, 4, 5, 6, 7]}
    a_dict[key] = value
#a_dict = {1: [2, 4, 6, 8, 10, 12], 2: [6, 9, 12, 15, 18, 21]}


b_dict = {1:1,2:2}
for key,value in b_dict.items():
    if key ==1:
        value = 3
    else:
        value = 4
    # b_dict[key] = value，字典才会改变
print('b_dict=',b_dict)

for value in b_dict.values():
    if value==1:
        value = 3
    else:
        value = 4
    # b_dict = value，字典才会改变
print("b_dict=",b_dict)
#修改字典的值
#method 1：
for key in b_dict.keys():
    if key ==1:
        b_dict[key] = 3
    else:
        b_dict[key] = 4
print("b_dict=",b_dict)
#method 2:
b_dict[1] = 5
print(b_dict)
