def selection_sort(arr):
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i,len(arr)):
            if int(arr[j]) < int(arr[minimum]):
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]

input_file = open('E:\input2.txt','r')
output_file = open('E:\output2.txt','w')
x = input_file.readline().strip()
y = x.split(' ')
z = input_file.readline().strip()
r = z.split(' ')
selection_sort(r)
for k in range(int(y[1])):
    print(r[k],end=' ',file=output_file)
output_file.close()
input_file.close()