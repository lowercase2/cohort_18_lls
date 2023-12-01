import doctest

def sum(a, b):
    """Returns integer addition of a and b

    >>> sum(4,6)
    10
    >>> sum(40,5)
    45
    >>> sum(40)
    Traceback (most recent call last):
        ...
    TypeError: sum() missing 1 required positional argument: 'b'



    """
    if(not isinstance(a, (int, float))):
        raise TypeError("A must be an integer or float")
    if(not isinstance(b, (int, float))):
        raise TypeError("B must be an integer or float")
    return int(a) + int(b)

sum(6,7)

doctest.testmod()