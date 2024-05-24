def sum_first_and_last_digit(n):
    # Convert the integer to a string
    str_num = str(n)

    # Get the first and last digit as characters
    first_digit = str_num[0]
    last_digit = str_num[-1]

    # Convert characters back to integers
    first_digit = int(first_digit)
    last_digit = int(last_digit)

    # Calculate the sum
    digit_sum = first_digit + last_digit

    return digit_sum

# Given integer numbers :
number = 12345
result = sum_first_and_last_digit(number)
print(f"The sum of the first and last digit of {number} is {result}")

