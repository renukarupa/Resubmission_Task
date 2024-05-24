def distribute_mangoes(mangoes, students):

    # Sort the list of mangoes in non-decreasing order
    mangoes.sort()
    # Initialize minimum difference to infinity
    min_diff = float('inf')
    # Initialize pointers
    left, right = 0, students - 1

    while right < len(mangoes):
        # Calculate difference between bags
        diff = mangoes[right] - mangoes[left]
        # Update minimum difference if smaller difference is found
        if diff < min_diff:
            min_diff = diff
        # Move left pointer forward
        left += 1
        # Move right pointer forward
        right += 1
    return min_diff


# Print the result:
mangoes = [3, 5, 8, 10, 14, 18, 20]
students = 3
min_difference = distribute_mangoes(mangoes, students)
print("Minimum difference between bags:", min_difference)