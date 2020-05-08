# palindrome
import math
import time
start = time.time()


def is_palindrome_v1(s):
    #print('Please insert the string: ')
    #s = input()
    if (s == reverse(s)):
        print('The string '+s+' is a palindrome')
        return True
    else:
        print('The string '+s+' is not a palindrome')
        return False

# reversiing a string


def reverse(s):
    rev = ''
    for chr in s:
        rev = chr+rev
    return rev


def is_palindrome_v2(s):
    n = len(s)
    if (s[:n//2] == reverse(s[n-n//2:])):
        print('The string '+s+' is a palindrome')
        return True
    else:
        print('The string '+s+' is not a palindrome')
        return False


def is_palindrome_v3(s):
    i = 0
    j = len(s)-1
    while (i < j and s[i] == s[j]):
        i = i+1
        j = j-1
    return j <= i


is_palindrome_v3('noon')
is_palindrome_v3('racecar')
is_palindrome_v3('dented')
is_palindrome_v3('ddddddddddddddddddddsdfsdfddddddddddddd')

print(time.time() - start)
