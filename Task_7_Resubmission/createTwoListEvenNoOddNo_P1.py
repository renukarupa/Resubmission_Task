# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize lists to hold even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the numbers and classify them as even or odd
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)