#思想：选择最大的跟最后一位交换，选择排序改进了冒泡排序，每个遍历列表只做一次交换，找出最大值与最后一位交换
def select_sort(data):
	for list_last in range(len(data)-1,0,-1):
		maxnum_index = 0
		for i in range(list_last):
			if data[i] > data[maxnum_index]:
				maxnum_index = i
		data[list_last], data[maxnum_index] = data[maxnum_index], data[list_last]#交换次数表少
		print('list_last: %s, data: %s'%(list_last,data))

data = [1,3,4,7,8,10,9,6,5,2,5]
select_sort(data)
#不稳定,i，j相同，最大值在i，j前面比如[10, 5, 5]
#时间复杂度，和冒泡有相同的比较次数，O(n2)
#空间复杂度O(1)
#额外空间：不需要
#