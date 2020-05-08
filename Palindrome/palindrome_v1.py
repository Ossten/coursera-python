import math
import time
start = time.time()

def is_palindrome_v1(s):
    #print('Please insert the string: ')
    #s = input()
    return reverse(s) == s

def reverse(s):
    rev = ''
    for chr in s: 
        rev = chr+rev
    return rev


if  __name__ == '__main__':
    print('In version 1, the module hame is: ', __name__)
    word  = input('Enter a word: ')
    if is_palindrome_v1(word):
        print(word,' is palindrome.')
    else:
        print(word,' is not a palindrome.')

    # is_palindrome_v1('noon')
    # is_palindrome_v1('racecar')
    # is_palindrome_v1('dented')
    print('Executed in : ',time.time() - start,'s.')
