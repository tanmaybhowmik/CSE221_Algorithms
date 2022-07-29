def LCS_Task_02(x, y, z):
    m = len(x) + 1
    n = len(y) + 1
    o = len(z) + 1
    c = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                    c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                else:
                    if c[i - 1][j][k] >= c[i][j - 1][k]:
                        maxi = c[i - 1][j][k]
                        if maxi >= c[i][j][k - 1]:
                            c[i][j][k] = maxi
                        else:
                            maxi = c[i][j][k - 1]
                            c[i][j][k] = maxi
                    else:
                        maxi = c[i][j - 1][k]
                        if maxi >= c[i][j][k - 1]:
                            c[i][j][k] = maxi
                        else:
                            maxi = c[i][j][k - 1]
                            c[i][j][k] = maxi
    return c[len(x)][len(y)][len(z)]


input_file = open('E:\input2.txt', 'r')
output_file = open('E:\output2.txt', 'w')
p = input_file.readlines()
a = p[0].strip()
b = p[1].strip()
c = p[2].strip()
y = LCS_Task_02(a, b, c)
print(y, file=output_file)
input_file.close()
output_file.close()