def find_second_largest(arr):
    n=len(arr)
    if n < 2:
        return -1

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num!=first:
            second = num

    if second==float('-inf'):
        return -1
    else:
        return second


arr = [12, 35, 1, 10, 34, 1,35, 10, 1]
# arr=[7,7,7]
print("Second largest element is:", find_second_largest(arr))