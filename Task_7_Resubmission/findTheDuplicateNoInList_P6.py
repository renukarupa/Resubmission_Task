# Define three lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 7, 8, 9, 10]

# Convert the lists to sets to remove duplicates within each list and allow for set operations
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find the intersection of the three sets to get the common elements
common_elements = set1.intersection(set2).intersection(set3)

# Convert the set back to a list (if needed)
duplicates = list(common_elements)

# Print the three list
print("list1", list1)
print("list2", list2)
print("list3", list3)

# Print the results
print("Duplicates in the three lists:", duplicates)
