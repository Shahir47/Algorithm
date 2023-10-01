def L_Convex_S(A, prev, cur, next, flag):
    if next > len(A) - 1:
        return 0
    if prev>=cur:
        return 0
    if cur>=next:
        return 0
    

    ignore = max(L_Convex_S(A, prev+1, cur, next, flag), L_Convex_S(A, prev, cur+1, next, flag), L_Convex_S(A, prev, cur, next+1, flag))
    best = ignore

    if A[prev]+A[next] > 2*A[cur]:
        if flag == 0:
            flag = 1
            include = 3 + L_Convex_S(A, cur, next, next+1, flag)
        else:
            include = 1 + L_Convex_S(A, cur, next, next+1, flag)
        #print(include, "prev: ", prev, cur, next)
        if include > best:
            best = include
    
    return best

flag = 0
print(L_Convex_S([1,2,3,14,5], 0, 1, 2, flag))
print(L_Convex_S([1,2,4,8,10,13], 0, 1, 2, flag))
print(L_Convex_S([1,3,2,2,4,1], 0, 1, 2, flag))
print(L_Convex_S([11,2,3,10], 0, 1, 2, flag))
print(L_Convex_S([11,2,3,7], 0, 1, 2, flag))
print(L_Convex_S([11,20,3], 0, 1, 2, flag))
print(L_Convex_S([3,2,2], 0, 1, 2, flag))