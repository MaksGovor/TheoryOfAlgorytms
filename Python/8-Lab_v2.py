from collections import namedtuple

Thing = namedtuple('Thing', 'price weight')

things = Thing(4, 5), Thing(3, 4), Thing(3, 2), Thing(2, 1)
CAPACITY = 10

def betterThing(items, weihgtLimit, things) :
  if items == 0 :
    return 0
  elif things[items - 1].weight > weihgtLimit :
      return betterThing(items - 1, weihgtLimit, things)
  else : 
      return max(
          betterThing(items - 1, weihgtLimit, things),
          betterThing(items - 1, weihgtLimit - things[items - 1].weight, things)
          + things[items - 1].price)

res = []
weihgtLimit = CAPACITY

for i in reversed(range(len(things))):
  if betterThing(i + 1, weihgtLimit, things) > betterThing(i, weihgtLimit, things):
    res.append(things[i])
    weihgtLimit -= things[i].weight

print(res)
