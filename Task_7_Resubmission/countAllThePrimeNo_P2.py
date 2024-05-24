# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Initialize list to hold prime numbers
prime_numbers = []

# Iterate through the numbers and check for primes
for number in numbers:
    if is_prime(number):
        prime_numbers.append(number)

# Count the number of prime numbers
prime_count = len(prime_numbers)

# Print the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)