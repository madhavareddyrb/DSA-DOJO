def sum_arr(arr):
    sum = 0
    for i in range(0,len(arr)):
        print(arr[i], "i")
        sum += arr[i]
        print(sum, "sum")

        arr[i] = sum
        print(arr, "agdgad")
    return arr


arr = [1, 2, 3, 4, 5]
print(sum_arr(arr))
