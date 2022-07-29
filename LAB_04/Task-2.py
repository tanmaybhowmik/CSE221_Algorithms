import queue
import math

def Dijkstra(Graph, source):
    dist = ['null', 0]
    visited = []
    for i in range(0, len(Graph) + 1):
        visited.append(False)
    Q = queue.PriorityQueue()
    for i in range(2, len(Graph) + 1):
        dist.append(float('inf'))
    prev = []
    for i in range(0, len(Graph) + 1):
        prev.append('null')
    j = 1
    for i in Graph:
        Q.put((dist[j], i))
        j = j + 1
    while not Q.empty():
        u = Q.get()[1]
        if visited[int(u)]:
            continue
        visited[int(u)] = True
        for x in Graph[u]:
            v = x[0]
            alt = dist[int(u)] + int(x[1])
            if alt < dist[int(v)]:
                dist[int(v)] = alt
                prev[int(v)] = u
                Q.put((dist[int(v)], v))
    m = []
    j = len(Graph)
    m.append(str(j))
    while j != 1:
        y = prev[j]
        m.append(y)
        j = int(y)

    return m

def graph(x):
    j = 1
    while j < len(x):
        tdict = {}
        b = x[j].split()
        for k in range(1, (int(b[0]) + 1)):
            tdict[str(k)] = []

        for k in range((j + 1), (j + int(b[1]) + 1)):
            t = x[k].split()
            tdict[t[0]].append((t[1], t[2]))
            tdict[t[1]].append((t[0], t[2]))
        h = Dijkstra(tdict, '1')
        l = len(h) - 1
        for n in range(l, -1, -1):
            print(h[n], end=' ', file = output_file)
        print('', file = output_file)
        j = j + int(b[1]) + 1

input_file = open('E:\input1.txt', 'r')
output_file = open('E:\output2.txt', 'w')
r = input_file.readlines()
g = graph(r)
input_file.close()
output_file.close()