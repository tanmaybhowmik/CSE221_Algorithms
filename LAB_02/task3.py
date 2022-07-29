def insertion_sort(a,b):
    for i in range(len(a)-1):
        temp = a[i+1]
        t = b[i+1]
        j = i
        while(j >= 0):
            if int(a[j]) < int(temp):
                a[j+1] = a[j]
                b[j+1] = b[j]
            else:
                break
            j = j-1
        a[j+1] = temp
        b[j+1] = t
    return b
input_file = open('E:\input3.txt','r')
output_file = open('E:\output3.txt','w')
m = input_file.readline()
n = input_file.readline().strip()
b = n.split(' ')
x = input_file.readline().strip()
a = x.split()

s = insertion_sort(a,b)
for i in range(0,len(s)):
    print(b[i],end=' ',file=output_file)
output_file.close()
input_file.close()