from collections import namedtuple

Median = namedtuple('Median', 'length value')

def heapify(nums, heapSize, rootIndex):  
    largest = rootIndex
    leftChild = (2 * rootIndex) + 1
    rightChild = (2 * rootIndex) + 2
    
    if leftChild < heapSize and nums[leftChild] > nums[largest]:
        largest = leftChild
    
    if rightChild < heapSize and nums[rightChild] > nums[largest]:
        largest = rightChild
    
    if largest != rootIndex:
        nums[rootIndex], nums[largest] = nums[largest], nums[rootIndex]
        heapify(nums, heapSize, largest)

def heapSort(nums):  
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def findMedian(element):
    arr.append(element)
    heapSort(arr)
    length = len(arr)
    if (length == 1): return Median(length, [arr[0]])
    if (length % 2 == 0):
      return Median(length, [arr[int(length / 2 - 1)], arr[int(length / 2)]])
    if (length % 2 != 0):
      return Median(length, [arr[int(length / 2)]])     

testArray = [1, 4, 5, 6, 3, 2, 10, 11, 14, 18, 12, 17]

res = []
arr = []

for i in testArray:
    res.append(findMedian(i))
print(res)
