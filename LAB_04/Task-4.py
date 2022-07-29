import queue
import math

def Dijkstra(Graph, source):
    Q = queue.PriorityQueue()
    dist = []
    prev = []
    for i in range(0, len(Graph) + 1):
        dist.append(-math.inf)
        prev.append('null')
    dist[int(source)] = math.inf
    for i in Graph:
        Q.put(((-1 * dist[int(i)]), i))
    while not Q.empty():
        u = Q.get()[1]
        for k in Graph[u]:
            alt = min(dist[int(u)], int(k[1]))
            if alt > dist[int(k[0])]:
                dist[int(k[0])] = alt
                prev[int(k[0])] = u
                Q.put((dist[int(k[0])], k[0]))
    dist[int(source)] = 0
    for k in range(0, len(dist)):
        if dist[k] == -math.inf:
            dist[k] = -1
    return dist

def graph(x):
    j = 1
    while j < len(x):
        tdict = {}
        b = x[j].split()
        for k in range(1, (int(b[0]) + 1)):
            tdict[str(k)] = []
        for i in range(j + 1, (j + int(b[1]) + 1)):
            t = x[i].split()
            tdict[t[0]].append((t[1], t[2]))
        h = Dijkstra(tdict, x[j + int(b[1]) + 1])
        for m in range(1, len(h)):
            print(h[m], end=' ', file = output_file)
        print('', file = output_file)
        j = j + int(b[1]) + 2

input_file = open('E:\input4.txt', 'r')
output_file = open('E:\output4.txt', 'w')
r = input_file.readlines()
g = graph(r)
input_file.close()
output_file.close()