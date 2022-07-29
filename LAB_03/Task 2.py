import queue
def BFS(graph, inode, enode):
    d = [-1] * (int(enode) + 1)
    p = ['null'] * (int(enode) + 1)
    color = ['white'] * (int(enode) + 1)
    for i in range(1, (len(graph) + 1), 1):
        if color[i] == 'white' and color[int(enode)] != 'black':
            BFS_1(graph, i, enode, d, p, color)

def BFS_1(h, v, l, d, p, color):
    q = queue.Queue(maxsize=int(l))
    color[v] = 'gray'
    d[v] = d[v - 1] + 1
    p[v] = 'null'
    w = str(v)
    q.put(w)
    while q is not None:
        u = q.get()
        print(u, end=' ', file=output_file)
        if u == l:
            color[int(u)] = 'black'
            break

        for j in h[u]:
            if color[int(j)] == 'white':
                color[int(j)] = 'gray'
                p[int(j)] = u
                d[int(j)] = d[int(u)] + 1
                q.put(j)
        color[int(u)] = 'black'

def graph_builder(x):
    tdict = {}
    for i in range (1, int(x[0])+1, 1):
        r = x[i].split()
        t = []
        for j in range (1, len(r), 1):
            t.append(r[j])
        tdict[r[0]] = t
    return tdict

input_file = open('E:\input1.txt','r')
output_file = open('E:\output2.txt','w')
s = input_file.readlines()
g = graph_builder(s)
BFS(g, '1', '12')
input_file.close()
output_file.close()