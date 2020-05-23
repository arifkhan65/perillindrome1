# NITIN
str_1 = "NITIN"
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print(is_palindrome(str_1))