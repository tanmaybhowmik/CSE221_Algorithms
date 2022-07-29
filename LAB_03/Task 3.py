def DFS(graph, enode):
    color = ['white'] * (int(enode) + 1)
    p = ['null'] * (int(enode) + 1)
    d = [0] * (int(enode) + 1)
    f = [0] * (int(enode) + 1)
    time = 0
    for i in range(1, (len(graph) + 1), 1):
        if color[int(enode)] != 'white':
            break
        elif color[i] == 'white':
            DFS_VISIT(graph, enode, i, color, p, d, f, time)


def DFS_VISIT(graph_1, des, v, color, p, d, f, time):
    color[v] = 'gray'
    time = time + 1
    d[v] = time
    w = str(v)
    print(w, end=' ', file=output_file)
    if w == des:
        return
    for j in graph_1[w]:
        if color[int(des)] != 'white':
            break
        elif color[int(j)] == 'white':
            p[int(j)] = w
            DFS_VISIT(graph_1, des, int(j), color, p, d, f, time)
    color[v] = 'black'
    time = time + 1
    f[v] = time


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
output_file = open('E:\output3.txt','w')
s = input_file.readlines()
g = graph_builder(s)
DFS(g, '12')
input_file.close()
output_file.close()