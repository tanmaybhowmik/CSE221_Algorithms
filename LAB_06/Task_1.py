import queue

def assignments(a):
    arr = []
    for i in range(int(a[0])):
        q = a[i+1].split(' ')
        l = [int(q[0]), int(q[1])]
        arr.append(l)
    #print(arr)
    cr = sorted(arr, key = lambda x: (x[1],x[0]))
    #print(cr)
    u = queue.Queue()
    u.put(cr[0])
    f = cr[0][1]
    count = 1
    for j in range(1,len(cr)):
        if cr[j][0]>f or cr[j][0] == f:
            count = count+1
            u.put(cr[j])
            f = cr[j][1]
        else:
            continue
    print(count, file = output_file)
    while not u.empty():
        r = u.get()
        print(r[0],r[1],file = output_file)

input_file = open('E:/task1_input.txt','r')
output_file = open('E:/output1.txt','w')
p = input_file.readlines()
y = assignments(p)
input_file.close()
output_file.close()