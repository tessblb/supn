def get_count_sum(nums, k):
    count_sum = [0] * k
    for num in nums:
        count_sum[num] += 1

    for i in range(1, k):
        count_sum[i] += count_sum[i - 1]
    return count_sum


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
