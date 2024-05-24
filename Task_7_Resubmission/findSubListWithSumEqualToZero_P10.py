def sub_list_with_zero_sum(nums):
    prefix_sum = 0
    seen = {}
    start_index = -1

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == 0:
            start_index = 0
            end_index = i
            return nums[start_index:end_index + 1]
        elif prefix_sum in seen:
            start_index = seen[prefix_sum] + 1
            end_index = i
            return nums[start_index:end_index + 1]
        else:
            seen[prefix_sum] = i

    return []

# Print the result:
numbers = [4, 2, -3, 1, 6]
result = sub_list_with_zero_sum(numbers)
if result:
    print("Sublist with sum equal to zero:", result)
else:
    print("There is no sublist with sum equal to zero.")
