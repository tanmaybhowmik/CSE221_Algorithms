def MERGE(b,d):
    sum = len(b)+len(d)
    c = []
    for i in range(0,sum,1):
        c.append(0)
    i = 0
    j = 0
    k = 0
    while len(b)!=0 and len(d)!=0:
        if int(b[i]) < int(d[j]):
            c[k] = b[i]
            b.pop(i)
        elif int(d[j]) < int(b[i]):
            c[k] = d[j]
            d.pop(j)
        k = k+1
    if len(b)!=0:
        e = b
    else:
        e = d
    for t in range(0,len(e)):
        c[k] = e[t]
        k = k+1
    return c
def MERGE_SORT(a,l,r):
    if l == r:
        p = []
        p.append(a[l])
        return p
    else:
        q = (l+r)//2
        a1 = MERGE_SORT(a,l,q)
        a2 = MERGE_SORT(a,q+1,r)
        f = MERGE(a1,a2)
    return f

input_file = open('E:\input4.txt','r')
output_file = open('E:\output4.txt','w')
n = input_file.readline().strip()
m = input_file.readline().strip()
r = m.split(' ')

q = MERGE_SORT(r,0,len(r)-1)
for g in range(0,len(q),1):
    print(q[g],end=' ',file=output_file)
input_file.close()
output_file.close()