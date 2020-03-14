arr = [
  [1, 4, 5, 3, 2],
  [2, 3, 4, 1, 5],
  [1, 4, 5, 3, 2],
  [3, 4, 5, 1, 2],
]

def comparison (matrix, x):
  results = []
  for i in range(len(matrix)):
    if i != x:
      c = 0
      cArr = matrix[i].copy()
      for j in range(len(matrix[x])):
        for k in range(len(cArr)):
          if matrix[x][j] == cArr[k]:
            if j != k :
              c += 1
              cArr[j], cArr[k] = cArr[k], cArr[j]
      results.append([i, c])
  return results

p = comparison(arr, 0)
print(p)