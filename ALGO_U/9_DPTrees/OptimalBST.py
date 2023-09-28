#Recursive Solution ---------------------------------------------------------------
def optimal_bst(A, F, i, j): 
    if j<i:
        return 0
    s = 0
    for ind in range(i, j+1):
        s += F[ind]

    best = optimal_bst(A, F, i, i-1) + optimal_bst(A, F, i+1, j)
    for r in range(i+1, j+1):
        best = min(best, optimal_bst(A, F, i, r-1) + optimal_bst(A, F, r+1, j))

    return best + s

# Dynamic Programming -----------------------------------------------------------
import math

def DP(A, F):
    n = len(A)
    mem = [[0]*n for i in range(n)]

    for i in range(n):
        mem[i][i] = F[i]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            best = math.inf
            s = 0
            for r in range(i, j+1):
                s += F[r]
                if r-1<0:
                    best = min(best, mem[r+1][j])
                elif r+1>=n:
                    best = min(best, mem[i][r-1])
                else:
                    best = min(best, mem[i][r-1]+mem[r+1][j])
            mem[i][j] = best + s

    for i in range(len(mem)):
        for j in range(len(mem[0])):
            print(mem[i][j], end=" ")
        print()

    return mem[0][n-1]

A = [2,5,7,8,14]
F = [100,2,4,10,4]

#print(optimal_bst(A, F, 0, len(A)-1))

print(DP(A, F))