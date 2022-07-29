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
output_file = open('E:\output1.txt','w')
s = input_file.readlines()
g = graph_builder(s)
print(g, file= output_file)
input_file.close()
output_file.close()