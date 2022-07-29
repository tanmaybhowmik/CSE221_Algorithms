import queue

def sequence(s):
    v = s[2]
    arr = []
    u = s[1].split()
    for i in range(int(s[0])):
        arr.append(int(u[i]))
    arr.sort()
    ja_c = queue.PriorityQueue()
    sequence_1 = []
    jack = []
    jill = []
    index = 0
    for i in v:
        if i == "J":
            ja_c.put(((-1 * index), arr[index]))
            jack.append(arr[index])
            sequence_1.append(arr[index])
            index = index + 1
        elif i == "j":
            x = ja_c.get()[1]
            jill.append(x)
            sequence_1.append(x)
    sum1 = 0
    sum2 = 0
    for i in range(len(jack)):
        sum1 = sum1 + jack[i]
    for i in range(len(jill)):
        sum2 = sum2 + jill[i]
    for i in sequence_1:
        print(i, end='', file=output_file)
    print(file=output_file)
    print('Jack will work for', sum1, 'hours', file=output_file)
    print('Jill will work for', sum2, 'hours', file=output_file)

input_file = open('E:/task3_input.txt', 'r')
output_file = open('E:/output3.txt', 'w')
p = input_file.readlines()
r = sequence(p)
input_file.close()
output_file.close()