#write a program to find the factorial of a nummber
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
        
number = 5
print(f'The factorial of {number} is {factorial_recursive(number)}.')
