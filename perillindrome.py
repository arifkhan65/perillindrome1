# NITIN
str_1 = "NITIN"
def is_palindrome(str_1):
    str_1 = str_1.lower()
    return str_1 == str_1[::-1]
print(is_palindrome(str_1))