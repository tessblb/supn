def get_count_sum(nums, k):
    # Initialize count array
    countSum = [0] * (k)

    # Store the count of each elements in count array
    for i in range(len(nums)):
        countSum[nums[i]] += 1

    # Store the cummulative count
    for i in range(1, k):
        countSum[i] += countSum[i - 1]

    return countSum


def get_counting_sort(nums, k):
    # sorts the list nums,
    # whose numbers are positive integer and less than or equal to N-1
    # via a linear time complexity algorithm

    count_sum = get_count_sum(nums, k)
    output = [0] * len(nums)

    for num in nums:
        output[count_sum[num] - 1] = num
        count_sum[num] -= 1

    return output
