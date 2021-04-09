import math
from config import Config

def atan_norm(value):
    """The arctan function grows more and more slowly as its input
       increases, so it is applied in hope of reducing the influence
       of possible outliers.

    Args:
        value (int): Byte frequency of a byte integer between 0-255.

    Returns:
        float: arctan norm of the x value.
    """
    return (math.atan(value) * (2.0 / math.pi)) + 1.0

def min_max_norm(value, min_val, max_val):
    """Constrains the weights incident to each hidden unit to have
       the norm between a lower bound and an upper bound.

    Args:
        value (float): Count value.
        min_val (int): Minimum value in count vector.
        max_val (int): Maximum value in count vector.

    Returns:
        float: A norm between a lower bound and an upper bound.
    """
    return (value - min_val) / (max_val - min_val)

def beta(value, min_val, max_val):
    """Rounds to down the normalized value.

    Args:
        value (int): Value that is wanted to normalize.
        min_val (float): Minimum value of the count vector.
        max_val (float): Maximum value of the count vector.

    Returns:
        str: Rounded down of the normalized value.
    """
    return math.floor(min_max_norm(value, min_val, max_val) * (-Config.MAX_UNSIGNED_BYTE_VAL) + Config.MAX_UNSIGNED_BYTE_VAL)

