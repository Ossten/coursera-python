
# LINEAR SEARCH--------------------------------------------------------------

def linear_search(arr, el):
    """(list, object) -> int
    Return the index of a first occurrance of el in arr, 
    or return -1 if the el is not in arr.

    >>> linear_search([2, 3, 5, 3], 2)
    0
    >>> linear_search([2, 3, 5, 3], 5)
    2
    >>> linear_search([2, 3, 5, 3], 8)
    -1
    """
    i = 0
    length = len(arr)
    while i != length and el != arr[i]:   # comparison  -> 2 steps per itteration (O(n) = n)
        i = i+1                             # asingment
    if i == length:
        return -1
    else:
        return i

#BINARY SEARCH --------------------------------------------------------------

def binary_search(arr, el):
    """(list, object) -> int

    Precondition : arr is sorted from smallest to largest, 
    and all items in arr can be comparet to el.

    Return the index of a first occurrance of el in arr, 
    or return -1 if the el is not in arr.

    >>> binary_search([2, 3, 5, 3], 2)
    0
    >>> binary_search([2, 3, 5, 3], 5)
    2
    >>> binary_search([2, 3, 5, 3], 8)
    -1
    """

    b = 0
    e = len(arr)-1

    while b<=e:                 #comparison 
        m = (b+e)//2            #asingment ->    4 steps per itteration  (O(n) = log2(n))
        if arr[m] < el:         #comparison
            b = m + 1           #
        else:                   # 1 comparison
            e = m - 1           #
    if b==len(arr) or arr[b]!= el:
        return -1
    else:
        return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# ANALISYS -----------------------------------------------------------

import cProfile

L= list(range(1000000))
print (len (L))
cProfile.run('binary_search(L, 1000001)')
cProfile.run('linear_search(L, 1000001)')