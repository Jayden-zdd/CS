alist = [1,2,3,4,5]
sumK = 6
gapK = 2
result_sum = []
result_gap = []
for i,value in enumerate(alist):
    if (sumK-value) in alist[i+1:]:
        result_sum.append((value,sumK-value))
    if (gapK+value) in alist[i+1:]:
        result_gap.append((value,gapK+value))
print(result_sum,len(result_sum))
print(result_gap,len(result_gap))

