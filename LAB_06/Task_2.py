def activities(n,m,a):
    arr = []
    for i in range(n):
        q = a[i+1].split(' ')
        l = [int(q[0]),int(q[1])]
        arr.append(l)
    cr = sorted(arr,key = lambda x: (x[1],x[0]))
    lt = []
    f = [0]*m
    for i in range(0,len(cr)):
        for j in range(len(f)):
            if cr[i][0]>f[j] or cr[i][0] == f[j]:
                lt.append(cr[i])
                f[j] = cr[i][1]
                break
    return len(lt)

input_file = open('E:/task2_input.txt','r')
output_file = open('E:/output2.txt','w')
p = input_file.readlines()
r = p[0].split()
o = activities(int(r[0]), int(r[1]), p)
print(o, file = output_file)
input_file.close()
output_file.close()