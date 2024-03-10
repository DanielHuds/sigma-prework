test_list = [1, 3, 5, -6, 99, 100]


def find_highest_and_lowest(nums):

    max = nums[0]
    min = nums[0]

    for num in nums:
        if num > max:
            max = num
        elif num < min:
            min = num

    return [min, max]


print(find_highest_and_lowest(test_list))
