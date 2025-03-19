
def InsertionSort(arr):

    for i in range(1, len(arr)):

        n = i

        while arr[n] < arr[n-1] and n > 0:
            arr[n], arr[n-1] = arr[n-1], arr[n]
            n -= 1

    return arr


arr = [1,5,2,4,3,7]

print(f"Before Sort: {arr}")
InsertionSort(arr)
print(f"After Sort: {arr}")