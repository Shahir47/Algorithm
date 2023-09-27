#Longest Increasing Subsequence -> This code returns the count of LIS

import math

#Recursive Solution -----------------------------------------------------
def LIS(arr, prev, start):
    if start>len(arr)-1:
        return 0
    
    ignore = LIS(arr, prev, start+1)
    best = ignore

    if prev==-math.inf or arr[start]>arr[prev]:
        include = 1 + LIS(arr, start, start+1)

        if include>ignore:
            best = include

    return best


#Iterative Solution ----------------------------------------------------

def LIS_Iterative(arr):
    arr.insert(0, -math.inf)
    print(arr)
    n = len(arr) + 1
    mem = [[None] * (n) for i in range(n-1)]

    for i in range (n-1):
        mem[i][n-1] = 0

    for start in range(n-2, -1, -1):
        for prev in range(0, start, 1):
            ignore = mem[prev][start+1]
            best = ignore
            if prev == 0 or arr[prev] < arr[start]:
                include = 1 + mem[start][start+1]
                if include > best:
                        best = include

            mem[prev][start] = best
    
    for i in range(len(mem)):
        for j in range(len(mem[0])):
            if mem[i][j] == None: print(0, end=" ")
            else: print(mem[i][j], end=" ")
        print()
    
    return mem[0][1]

myArr = [10,5,9,6,8,3,12]
#print(LIS(myArr, -math.inf, 0))
print(LIS_Iterative(myArr))
