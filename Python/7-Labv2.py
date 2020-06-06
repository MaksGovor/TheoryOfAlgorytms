answer = [] 

def TravellingSalesman(graph, vertexFlags, currPos, n, count, distance): 

    if (count == n and graph[currPos][0]): 
        answer.append(distance + graph[currPos][0])
        return

    for i in range(n): 
        if (not vertexFlags[i] and graph[currPos][i]):
            vertexFlags[i] = True
            TravellingSalesman(graph, vertexFlags, i, n, count + 1,distance + graph[currPos][i])
            vertexFlags[i] = False

# Usage

graph= [[ 0, 40, 15, 10 ], 
        [ 40, 0, 25, 25 ], 
        [ 15, 25, 0, 50 ],
        [ 10, 25, 50, 0 ]] 

v = [False for i in range(len(graph))]
v[0] = True

TravellingSalesman(graph, v, 0, len(graph), 1, 0)

print(answer)
print('Min route = ' + str(min(answer)))