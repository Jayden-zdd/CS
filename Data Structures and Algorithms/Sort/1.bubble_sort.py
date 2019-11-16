#思想：两两比较，每次遍历作n-1次比较，有多次交换
def bubble_sort(data):
	for list_last in range(len(data)-1,0,-1):
		for i in range(list_last):
			if data[i] > data[i+1]:
				# temp = data[i+1]
				# data[i+1] = data[i]
				# data[i] = temp
				data[i], data[i+1] = data[i+1], data[i]#python不需要额外的内存空间
		print("list_last:{},data:{}".format(list_last,data))
data = [5,1,3,4,7,8,10,9,6,2,5]
bubble_sort(data)
# print(data)

#稳定 if data[i] > data[i+1] 不是等于
#时间复杂度O(n2) = (n-1) + (n-2) +... + 1 ,
#空间复杂度O(1)
#额外空间：不需要
#最佳情况：O(n)算法可以改进
