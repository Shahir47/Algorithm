inversion = 0

def merge(arr, l, r):
    global inversion
    temp = [None]*((r-l)+1)
    k = 0

    m = l + (r-l)//2
    i = l
    j = m+1
    while i<=m and j<=r:
        if arr[i]<arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
            inversion += m+1-i #m+1 is the size of left array. Now when arr[j]<arr[i] arr[j] will sit before the m+1-i values. This is 
                                # also the number of inversions needed in the unsorted array.
    while i<=m:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j<=r:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    k = 0
    for i in range (l, r+1, 1):
        arr[i] = temp[k]
        k += 1
        
    return arr


def mergeSort(arr, l, r):
    if r-l>0:
        m = l + (r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        return merge(arr, l, r)

arr_ = [5,4,3,2,1]
print(mergeSort(arr_, 0, len(arr_)-1))
print(inversion) #it counts the number of inversions in the input array. Which is, each is the 
                    #number of j > i in the unsroted array where index-j < index-i
