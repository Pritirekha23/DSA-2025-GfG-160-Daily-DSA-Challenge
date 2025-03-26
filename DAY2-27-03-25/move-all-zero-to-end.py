# write a python function to move all zeroes to the end of the array without changing the order of non-zero elements

def move_zeros_to_end(arr):
    n = len(arr)
    count = 0  # Count of non-zero elements

    # Traverse the array. If the element is not zero, then
    # replace the element at index 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to the front
    # and 'count' is set as the index of the first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

# Example usage
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
move_zeros_to_end(arr)
print(arr)

# Output: [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
# Time Complexity: O(n)
# Space Complexity: O(1)
 
#App-2
def pushzero(arr):
    count=0

    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
            
arr=[0,8,9,7,4,0,0,2,6,0,6,0,9]
pushzero(arr)
for num in arr:
    print(num,end=" ")

# Output: 8 9 7 4 2 6 6 9 0 0 0 0 0
# Time Complexity: O(n)
# Space Complexity: O(1)