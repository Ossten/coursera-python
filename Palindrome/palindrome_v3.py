import math
import time
start = time.time()

def is_palindrome_v3(s):
    i = 0
    j = len(s)-1
    while (i < j and s[i] == s[j]):
        i = i+1
        j = j-1
    return j <= i


def reverse(s):
    rev = ''
    for chr in s:
        rev = chr+rev
    return rev


is_palindrome_v3('noon')
is_palindrome_v3('racecar')
is_palindrome_v3('dented')

print(time.time() - start)