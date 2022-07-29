def Multiply_Matrix(A, B):
    global n
    C = [[0] * n for i in range (n)]
    for i in range (0, n, 1):
        for j in range (0, n, 1):
            for k in range (0, n, 1):
                C[i][j] += int(A[i][k]) * int(B[k][j])
    return C
input_file = open('E:\input4.txt', 'r')
output_file = open('E:\output4.txt', 'w')
n = int(input_file.readline())
A = []
B = []
D = 0
while True:
    E = input_file.readline().strip()
    F = E.split(' ')
    if D == (2 * n) + 1:
        break
    if D < n:
        A.append(F)
    elif D > n:
        B.append(F)

    D = D + 1

C = Multiply_Matrix(A, B)
for l in range(0,len(C),1):
    for m in range(0,len(C[l]),1):
        print(C[l][m],end=' ',file=output_file)
    print('',file=output_file)
output_file.close()

print(A)
print(B)