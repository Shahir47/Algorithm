count = 0
def mergeSort(arr):
    global count
    n = len(arr)
    if n>1:
        m = n//2
        arr_left = arr[:m]
        arr_right = arr[m:]
        mergeSort(arr_left)
        mergeSort(arr_right)
        
        i = 0
        j = 0
        k = 0
        while i<len(arr_left) and j<len(arr_right):
            if arr_left[i]<arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
                count += len(arr_left)-i
            k += 1

        while i<len(arr_left):
                arr[k] = arr_left[i]
                i += 1
                k += 1
        while j<len(arr_right):
                arr[k] = arr_right[j]
                j += 1
                k += 1
        print(count)

count = 0
arr = [4,1,3,2]
mergeSort(arr)
print(arr)
print(count)