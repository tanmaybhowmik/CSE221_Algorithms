def LCS_Task_01(a):
    td={'Y':'Yasnaya','R':'Rozhok','S':'School','P':'Pochinki','F':'Farm','M':'Mylta','H':'Shelter','I':'Prison'}
    x=a[1].strip()
    y=a[2].strip()
    c=[[0 for i in range(int(a[0])+1)] for j in range(int(a[0])+1)]
    t=[[None for i in range(int(a[0])+1)] for j in range(int(a[0])+1)]
    for i in range(1,(int(a[0])+1)):
        for j in range(1,(int(a[0])+1)):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                t[i][j]='diagonal'
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                t[i][j]='up'
            else:
                c[i][j]=c[i][j-1]
                t[i][j]='left'
    correctness=(c[int(a[0])][int(a[0])]*100)/int(a[0])
    sequence=[]
    i=int(a[0])
    j=int(a[0])
    while t[i][j]!=None:
        if t[i][j]=='diagonal':
            sequence.append(x[i-1])
            i=i-1
            j=j-1
        elif t[i][j]=='up':
            i=i-1
        else:
            j=j-1
    for i in range((len(sequence)-1),-1,-1):
        print(td[sequence[i]],end=' ',file=output_file)
    print(file=output_file)
    print('Correctness of prediction:',correctness,'%',file=output_file)
input_file=open('E:\input1.txt','r')
output_file=open('E:\output1.txt','w')
p=input_file.readlines()
u=LCS_Task_01(p)
input_file.close()
output_file.close()