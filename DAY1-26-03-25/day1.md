## #gfg160 & #geekstreak2025.
## DAY-1 : 25/03/25 
### Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.
Note: If the second largest element does not exist, return -1.

```
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
print("Second largest element is:", find_second_largest(arr))

```

```
Input Array: [12, 35, 1, 10, 34, 1, 35, 10, 1]

Step 1: Process 12

first = 12 (largest so far)

second = -inf (no second largest yet)

Step 2: Process 35

35 is greater than first (12), so update:

second = 12

first = 35

Step 3: Process 1

1 is neither greater than first (35) nor greater than second (12), so no change.

Step 4: Process 10

10 is neither greater than first (35) nor greater than second (12), so no change.

Step 5: Process 34

34 is smaller than first (35), but greater than second (12), so update:

second = 34

Step 6: Process 1

1 is neither greater than first (35) nor second (34), so no change.

Step 7: Process 35

35 is equal to first (35), so no change.

Step 8: Process 10

10 is neither greater than first (35) nor second (34), so no change.

Step 9: Process 1

1 is neither greater than first (35) nor second (34), so no change.

At the end of the iteration:

Largest Element (first) = 35

Second Largest Element (second) = 34
```