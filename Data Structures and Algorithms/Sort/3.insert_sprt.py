#思想：就第一位构建有序子列表A，然后未排序列表跟有序列表后面的项依次比较插入，使得有序列表的后面部分后移

def insert_sort(data):
	for i in range(1, len(data)):
		current_value = data[i]
		position = i
		while position > 0 and data[position-1] > current_value:
			data[position] = data[position-1]
			position = position - 1 
		data[position] = current_value
		print('unsort 1th num inser %s'%(data))
data = [5,1,3,4,7,8,10,9,6,2,5]
insert_sort(data)

#稳定性：稳定
##时间复杂度：O(n2):n-1个数字需要排序，依次每个数字需要和1,2,3，...,n-1个数字比较，所以也是1 + 2 + 3 + ... + (n-1)
#空间复杂度O(1)
#额外空间：不需要
#最好情况：O(n)排好序的只需要对未排序的数据(n-1)个和以排序的最后一位比较一次