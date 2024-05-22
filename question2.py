# find if the given number is a palindrome or not?
def is_palindrome_number(n):
   
    s = str(n)

    return s == s[::-1]

test_number = int(input())
if is_palindrome_number(test_number):
    print(f'{test_number} is a palindrome.')
else:
    print(f'{test_number} is not a palindrome.')
