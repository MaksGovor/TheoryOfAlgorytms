def insertion (arr):
  for i in range(1, len(arr)):
    for j in range(i):
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
      if arr[j] % 2 != 0:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

arr = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41]

insertion(arr)

print(arr)