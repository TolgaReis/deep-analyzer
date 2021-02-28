import math

def atan_norm(x):
    """The arctan function grows more and more slowly as its input increases, 
       so it is applied in hope of reducing the influence of possible outliers.

    Args:
        x (int): Byte frequency of a byte integer between 0-255.

    Returns:
        float: arctan norm of the x value.
    """
    return (math.atan(x) * 2 / math.pi) + 1

def min_max_norm(x):

    return x