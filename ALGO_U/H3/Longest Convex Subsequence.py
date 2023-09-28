def L_Convex_S(A, prev, cur, next):
    if next > len(A) - 1:
        return 0
    
    ignore = max(L_Convex_S(A, prev, cur, next+1), L_Convex_S(A, prev, cur+1, next+1), L_Convex_S(A, prev+1, cur+1, next+1))
    best = ignore

    if A[prev]+A[next] > 2*A[cur]:
        print(A[prev], A[cur], A[next])
        include = 1 + max(L_Convex_S(A, prev+1, cur+1, next+1), L_Convex_S(A, prev, cur, next+1), L_Convex_S(A, prev, cur+1, next+1))
        if include > best:
            best = include
    
    return best


print(L_Convex_S([1,3,2,2,4,1], 0, 1, 2))