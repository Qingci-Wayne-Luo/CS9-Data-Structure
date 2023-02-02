# Week 6

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2

		# uses additional space to create the left / right
		# halves
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		# recursively sort the lefthalf, then righthalf
		mergeSort(lefthalf)
		mergeSort(righthalf)

		# merge two sorted sublists (left / right halves)
		# into the original list (alist)
		i = 0 # index for lefthalf sublist
		j = 0 # index for righthalf sublist
		k = 0 # index for alist

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k + 1
			print(alist, i, j, k)

		# put the remaining lefthalf elements (if any) into
		# alist
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		# put the remaining righthalf elements (if any) into
		# alist
		while j < len(righthalf):
			alist[k] = righthalf[j]
			j = j + 1
			k = k + 1


print(mergeSort([2, 5, 6, 8, 3, 4, 7, 10]))





'''def quickSort(alist):
	quickSortHelper(alist, 0, len(alist) - 1)

# helper function so we can pass in the first / last index
# of lists
def quickSortHelper(alist, first, last):
	if first < last:

		# will define the indices of the left / right sub lists
		splitpoint = partition(alist, first, last)

		# recursively sort the left / right sub lists
		quickSortHelper(alist, first, splitpoint-1) # left
		quickSortHelper(alist, splitpoint+1, last) # right

# partition function will organize left sublist < pivot
# and right sub list > pivot
def partition(alist, first, last):
	pivotvalue = alist[first] # choose first element as pivot

	leftmark = first + 1
	rightmark = last

	done = False
	while not done:

		# move leftmark until we find a left element > pivot
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		# move rightmark until we find a right element < pivot
		while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
			rightmark = rightmark - 1

		# check if we're done swapping left / right elements in
		# correct side
		if rightmark < leftmark:
			done = True
		else: # swap left and right elements into correct side of list
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
		print(alist, rightmark, leftmark)

	# put the pivot value into the correct place (swap pivot w/ rightmark)
	temp = alist[first] # pivot
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark

print(partition([3, 5, 2, 6, 1, 0],0,5))
'''















