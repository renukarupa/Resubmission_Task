def first_non_repeating(nums):
    # Create a dictionary to store the frequency of each element
    freq = {}

    # Count the frequency of each element in the list
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Iterate through the list again to find the first element with frequency 1
    for num in nums:
        if freq[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None


# Print the result:
numbers = [1, 2, 3, 4, 2, 3, 1, 5, 6]
result = first_non_repeating(numbers)
print("First non-repeating element:", result)
