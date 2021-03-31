n = int(input()) #размер матрицы
if n < 4 or n > 1000:
    print('Маловато будет!')
else:
    matrix = [[0]*n for i in range(n)]
    cur, m = 1, 0 #текущее значение
    matrix[n//2][n//2] = n*n
    for j in range(n//2):

        for i in range(n-m):
            matrix[j][i+j] = cur
            cur+=1

        for i in range(j+1, n-j):
            matrix[i][-j-1] = cur
            cur+=1

        for i in range(j+1, n-j):
            matrix[-j-1][-i-1] =cur
            cur+=1

        for i in range(j+1, n-(j+1)):
            matrix[-i-1][j]=cur
            cur+=1
        m+=2
    for i in matrix:
        print(*i)