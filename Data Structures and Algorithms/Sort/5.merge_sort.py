#思想：分而治之，递归实现，先自上而下的递归，然后自下而上的迭代
def merge_sort(alist):
	print('spliting:', alist)
	if len(alist) >1:
		mid = len(alist)//2
		left_list = alist[:mid]
		right_list = alist[mid:]
		merge_sort(left_list)
		merge_sort(right_list)
		#merge
		i=0
		j=0
		k=0
		while i < len(left_list) and j < len(right_list):
			if left_list[i] < right_list[j]:
				alist[k] = left_list[i]
				i = i + 1
			else:
				alist[k] = right_list[j]
				j = j + 1
			k = k + 1
		while  i < len(left_list):
			alist[k] = left_list[i]
			i = i + 1
			k = k + 1
			print('alist_i',alist)
		while  j < len(right_list):
			alist[k] = right_list[j]
			j = j + 1
			k = k + 1
			print('alist_j',alist)
		print('Merging:', alist)
alist = [5,1,3,4,7,8,10,9,6,2,5]
merge_sort(alist)

#稳定性：稳定
#时间复杂度：O(nlogn)
#空间复杂度：O(n)
#额外空间：需要