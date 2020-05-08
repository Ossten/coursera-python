def num_buses(n):
    import math
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2n
    >>> num_buses(110)
    3
    >>> num_buses(49)
    1
    """

    if n >= 0:
        return math.ceil(n / 50)
    else: return -1




def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    sumg = suml = 0
    for v in price_changes:
        if v >= 0 :
            sumg = sumg + v
        else:
            suml = suml + v
    return ((sumg, suml))

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    [5, 6, 3, 4, 1, 2]
    >>> nums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    >>> swap_k(nums, 3)
    ['g', 'h', 'j', 'd', 'e', 'f', 'a', 'b', 'c']
    """
   
    temp = 0
    if k >= 0 and k <= len(L)//2:
        for i in range (0, k):
            temp = L[i]
            L[i] = L[len(L)-k+i]
            L[len(L)-k+i] = temp
        return (L)
    else: return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()