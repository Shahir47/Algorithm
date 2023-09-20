#Recursive Solution:
#---------------------------------------------------------------------------
def rc(costArr, n, mem):
    if n==0:
        return 0
    if(mem[n-1]==None):
        q = 0
        for i in range(n):
            q = max(q, costArr[i]+rc(costArr, n-(i+1), mem))
        mem[n-1]=q


    return mem[n-1]

def rodCuttingRecursive(costArr, n):
    mem = [None]*n
    return rc(costArr, n, mem)

#---------------------------------------------------------------------------
#Iterative DP:
def rodCuttingIterative(costArr, n):
    if n==0:
        return 0
    mem = [None]*n
    cuts = [None]*n #it outputs the cut position

    q = 0

    for i in range(n):
            j = 0
            while j<i:
                if costArr[j]+mem[i-j-1]>q:
                    q = costArr[j]+mem[i-j-1]
                    cuts[i] = j

                j += 1
            if costArr[j]>q:
                q = costArr[j]
                cuts[i] = j

            mem[i] = q

    print("cuts->", cuts)
    #Try to determine the number of cuts!!! Such as, for the first problem it is 1 cut (2 or 6)
    return q

#----------------------------------------------------------------------------
print(rodCuttingIterative([1,5,8,9,10,17,17,20], 8)) #22
#print(rodCuttingIterative([3,5,8,9,10,17,17,20], 8)) #24
#print(rodCuttingRecursive([1,5,8,9,10,17,17,20], 8))

# Runtime of this algorithm is T(n)=Theta(n x n) where
#     first  n = table size
#     second n = time for table index entry