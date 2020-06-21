'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    max = 0
    n = len(nums)
    result = []

    for i in range(n - k + 1):
        max = nums[i]
        for j in range(1, k):
            if nums[i + j] > max:
                max = nums[i + j]
        result.append(max)

    return result



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")



### This was the code I was working on myself, before looking it up
#  # k counters
#     compareArr = nums[:k-1]
#     # number of windows    
#     num = len(nums) - (k-1)
#     # output
#     output = [0] * (num)
#     # compare each time
#     for i in range(0, num + 1):
#         maximum = max(compareArr)
#         # push max to output
#         output[i] = maximum
#         # move window
#         k += 1
#         compareArr = nums[i:k-1]


#     return output