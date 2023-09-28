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



A = [2,5,7,8,14]
F = [1,11,1,10,9]
print(optimal_bst(A, F, 0, len(A)-1))