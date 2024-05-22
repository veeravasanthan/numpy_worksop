#write a program to find if the given number is prime no or not
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
test_number = 29
if is_prime(test_number):
    print(f'{test_number} is a prime number.')
else:
    print(f'{test_number} is not a prime number.')
