#Recursive Solution -------------------------------------------------------
def LCS(arr1, arr2, s1, s2):
    if s1 > len(arr1)-1:
        return 0
    if s2 > len(arr2)-1:
        return 0
    
    ignore = max(LCS(arr1, arr2, s1+1, s2), LCS(arr1, arr2, s1, s2+1))
    best = ignore

    if arr1[s1] == arr2[s2]:
        include = 1 + LCS(arr1, arr2, s1+1, s2+1)
        if include>best:
            best = include
    
    return best

#Dynamic Programming -------------------------------------------------------
def LCS_Iterative(arr1, arr2):
    n = len(arr1) + 1
    m = len(arr2) + 1

    mem = [['N']*n for i in range(m)]

    for i in range(m):
        mem[i][n-1] = 0
    for i in range(n):
        mem[m-1][i] = 0

    for curA in range(n-2, -1, -1):
        for curB in range(m-2, -1, -1):
            ignore = max(mem[curB][curA+1], mem[curB+1][curA])
            best = ignore

            if arr1[curA] == arr2[curB]:
                include = 1 + mem[curB+1][curA+1]
                if best<include:
                    best = include  
            
            mem[curB][curA] = best
            
    for i in range(len(mem)):
        for j in range(len(mem[0])):
            print(mem[i][j], end=" ")
        print()

    return mem[0][0]

x = "CGCAATCCAGG"
y = "GATTACGA"
a = list(x)
b = list(y)


#print(LCS(a, b, 0, 0))

print(LCS_Iterative(a, b))