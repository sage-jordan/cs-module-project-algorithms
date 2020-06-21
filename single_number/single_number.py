'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # initiate maximum
    maximum = max(arr)


    # set up empty counter list
    counter = [0] * (maximum + 1)

    # iterate over arr, counting instances
    for num in arr:
        counter[num] += 1
    print(counter)
    # initiate j index
    j = 0

    # iterate over counted arr
    for i in counter:
        # return the number if only counted once
        if i == 1:
            return j
        # count index
        j += 1
    return False

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")



    # Tried this for range loop #### didn't work
    # for i in range(0, len(counter) + 1):
    #     while counter[i] != 1:
    #         j += 1
    #     return arr[j]


    # # iterate over counted arr ### didn't work
    # for i in range(0, len(counter) + 1):
    #     # if this index = 1
    #     if counter[i] == 1:
    #         # return array at this index
    #         return arr[j]
    #     # else, add to j index and try again
    #     else: j += 1
