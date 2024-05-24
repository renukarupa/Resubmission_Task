def find_triplet_with_sum(nums, target):
    # Sort the list
    nums.sort()

    # Iterate over the list to find the triplets
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    # If no triplet is found, return an empty list
    return []


# Print the result:
numbers = [10, 20, 30, 9]
target = 59
result = find_triplet_with_sum(numbers, target)
if result:
    print("Triplet with sum", target, ":", result)
else:
    print("No triplet found with sum", target)
