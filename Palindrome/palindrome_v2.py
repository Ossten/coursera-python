import math
import time
start = time.time()
from palindrome_v1 import reverse


def is_palindrome_v2(s):
    n = len(s)
    return(s[:n//2] == reverse.reverse(s[n-n//2:]))
    
       


# def reverse(s): 
#     rev = ''
#     for chr in s:
#         rev = chr+rev
#     return rev



print('In version 2, the module hame is: ', __name__)
# is_palindrome_v2('noon')
# is_palindrome_v2('racecar')
# is_palindrome_v2('dented')

print('Executed in : ',time.time() - start,'s.')