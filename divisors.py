def get_divisors(num,possible_divisors):
    '''
    >>> get_divisors(8,[1,2,3])
    [1, 2]
    >>> get_divisors(4, [-2, 0, 2])
    [-2, 2]
    '''
    divisors = []
    for item in possible_divisors:
        if item !=0 and num%item ==0:
            divisors.append(item)

    return divisors

import doctest
doctest.testmod()