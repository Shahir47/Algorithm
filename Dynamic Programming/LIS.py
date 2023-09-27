#Longest Increasing Subsequence -> This code returns the count of LIS
import math
def LIS(arr, prev, start, mem):
    if start>len(arr)-1:
        return 0
    
    ignore = LIS(arr, prev, start+1, mem)
    best = ignore

    if prev==-math.inf or arr[start]>arr[prev]:
        if mem[start][start+1] != None:
            include = mem[start][start+1]
        else:
            include = 1 + LIS(arr, start, start+1, mem)
            mem[start][start+1] = include
        if include>ignore:
            best = include
    return best

myArr = [10,5,9,6,8,3,12]
mem = [[None]*(len(myArr)+1) for i in range(len(myArr))] #[prev][start]
print(LIS(myArr, -math.inf, 0, mem))
print(mem)
