#希尔排序也是递减增量排序，是插入排序的改进版本，将列表分成多份列表，
#然后每份进行插入排序，再合并各份列表的结果，最终采用增量为1的插入排序
#这样操作减少了总共的移位操作总数

def shell_sort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gap_inser_sort(alist, startposition, sublistcount)
		print("after increments of size {}, the list is {}".format(sublistcount,alist))
		sublistcount = sublistcount//2

def gap_inser_sort(alist, start, gap):
	for i in range(start+gap,len(alist), gap):
		current_value = alist[i]
		position = i 

		while position > start and alist[position-gap] > current_value:
			alist[position] = alist[position - gap ]
			position = position - gap

		alist[position] = current_value 

alist = [5,1,3,4,7,8,10,9,6,2,5]
shell_sort(alist)

#稳定性：不稳定，[5 3 1 5 2]
#时间复杂度：O(nlogn)
#空间复杂度：O(1)
