## Sort1
alist1 = [54,26,93,17,77,31,44,55,20]
count1 = 0

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global count1
   pivotvalue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:
       
       if not (leftmark <= rightmark and alist[leftmark] <= pivotvalue): count1 += 1
       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           count1 += 1
           leftmark = leftmark + 1
       
       if not (leftmark <= rightmark and alist[rightmark] >= pivotvalue): count1 += 1
       while leftmark <= rightmark and \
              alist[rightmark] >= pivotvalue :
           count1 += 1
           rightmark = rightmark -1

       if leftmark > rightmark:
           done = True
       else:
           alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

   alist[first], alist[rightmark] = alist[rightmark], alist[first]

   return rightmark

quickSort(alist1)
print(alist1)

## Sort2 
alist2 = [54,26,93,17,77,31,44,55,20]
count2 = 0

def partition2(arr,low,high): 
    global count2
    i = ( low-1 )          
    pivot = arr[high]      
    for j in range(low , high): 
        count2 += 1 
        if   arr[j] <= pivot:  
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
   
def quickSort2(arr,low,high):
    if low < high:  
        pi = partition2(arr,low,high)  
        quickSort2(arr, low, pi-1) 
        quickSort2(arr, pi+1, high) 

quickSort2(alist2,0, len(alist2) - 1)
print(alist2)


## Sort3

alist3 = [54,26,93,17,77,31,44,55,20]
count3 = 0

def quickSort3(arr):
  global count3
  less = []
  pivotList = []
  more = []
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  for i in arr:
    p = 1 if i < pivot else 2
    count3 += p
    if i < pivot:
      less.append(i)
    elif i > pivot:
      more.append(i)
    else:
      pivotList.append(i)
    less = quickSort3(less)
    more = quickSort3(more)
  return less + pivotList + more

a = quickSort3(alist3)
print(a)

print({'sort1': count1, 'sort2': count2, 'sort3': count3})
