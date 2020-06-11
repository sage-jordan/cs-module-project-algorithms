'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0
    # Loop over arr
    for i in range(0, len(arr) ):
    # If current value is 0, .append the popped val
        if arr[i] != 0:
            # count is incrememnted
            arr[count] = arr[i]
            count += 1
    # now add 0s to the end
    while count < len(arr):
        arr[count] = 0
        count += 1
        
    # after loop, return arr
    print(arr)
    return arr ### err: returns after merging all 0s in last test

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")