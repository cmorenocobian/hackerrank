def maxMin (k,arr):
    arr.sort()
    minimun = 10 ** 10
    for i in range(len(arr)-k + 1):
        temp = arr[i+k-1] - arr[i]
        if temp < minimun:
            minimun = temp
    return minimun
