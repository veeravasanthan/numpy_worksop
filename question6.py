#write a program to find the maximum of two numbers
def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
num1 = 10
num2 = 20
maximum = find_maximum(num1, num2)
print(f'The maximum of {num1} and {num2} is {maximum}.')
