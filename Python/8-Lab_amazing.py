from itertools import combinations

max_w = 6
things = [(4, 5), (3, 4), (3, 2), (2, 1)]  

res = max(filter(lambda x: sum(list(zip(*x))[0]) <= max_w,\
    (v for r in range(1, len(things)) for v in combinations(filter(lambda x: x[0] <= max_w, things), r))),\
    key = lambda x: sum(list(zip(*x))[1]))

print(res)