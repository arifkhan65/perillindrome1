# NITIN
n=input('please input you data here to check if it is pellindrome:' )
def is_palindrome(n):
    n = n.lower()
    return n == n[::-1]
print('the result is:',is_palindrome(n))