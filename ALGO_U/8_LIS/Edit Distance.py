#Recursive Solution -------------------------------------------------------------------------------------
def edit_distance(A, B, n, m):
    if n < 0:
        return m+1
    if m < 0:
        return n+1
    
    insert = 1 + edit_distance(A, B, n, m-1)
    delete = 1 + edit_distance(A, B, n-1, m)
    substitute = edit_distance(A, B, n-1, m-1) if (A[n] == B[m]) else 1 + edit_distance(A, B, n-1, m-1)

    return min(insert, delete, substitute)

#Dynamic Programming ------------------------------------------------------------------------------------
def DP(A, B):
    A.insert(0, 0)
    B.insert(0, 0)
    n = len(A)
    m = len(B)

    mem = [[None]*(n) for i in range(m)] #A is in the row and B is in the column

    for i in range(n):
        mem[0][i] = i

    for i in range(m):
        mem[i][0] = i

    for curA in range(1, n):
        for curB in range(1, m):
            insert = 1 + mem[curB-1][curA]
            delete = 1 + mem[curB][curA-1]
            substitute = mem[curB-1][curA-1] if A[curA] == B[curB] else 1 + mem[curB-1][curA-1]

            mem[curB][curA] = min(insert, delete, substitute)
    
    for i in range(len(mem)):
        for j in range(len(mem[0])):
            print(mem[i][j], end=" ")
        print()

    return mem[m-1][n-1]

x = "FOOD"
y = "MONEY"
arr1 = list(x)
arr2 = list(y)

print(DP(arr1, arr2))

#print(edit_distance(arr1, arr2, len(arr1)-1, len(arr2)-1))