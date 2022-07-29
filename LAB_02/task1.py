def bubbleSort(arr):
    for i in range (len(arr)-1):
        swap_count = 0
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count = swap_count + 1
        if swap_count == 0:
            return arr
    return arr
input_file = open('E:\input1.txt','r')
output_file = open('E:\output1.txt','w')
x = input_file.readline().strip()
y = input_file.readline().strip()
z = y.split(' ')
s = bubbleSort(z)
for k in range(0,len(s),1):
    print(s[k],end=' ',file=output_file)
output_file.close()
input_file.close()