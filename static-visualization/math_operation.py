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

def min_max_norm(x, min, max):
    """Constrains the weights incident to each hidden unit to have the norm between a lower bound and an upper bound.

    Args:
        x (float): Count value.
        min (int): Minimum value in count vector.
        max (int): Maximum value in count vector.

    Returns:
        float: A norm between a lower bound and an upper bound.
    """
    return (x - min) / (max - min)