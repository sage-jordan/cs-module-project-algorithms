'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # If empty
    if len(arr) <= 1:
        return arr
    
    # Loop over arr
    for i in range(0, len(arr) - 1):
    # If current value is 0, .append the popped val
        if arr[i] == 0:
            popped = arr.pop(i)
            arr.append(popped)
            print('\n')
            print(popped)
        
        
    # after loop, return arr
    print(arr)
    return arr ### err: returns after merging all 0s in last test

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")