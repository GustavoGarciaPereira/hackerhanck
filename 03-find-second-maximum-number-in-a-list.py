


def segundo(n, arr):
    arr = list(set(arr))
    arr.sort(reverse=True)
    print(arr[1])
        
segundo(5, [2,3,6,6,5])