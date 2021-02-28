from math_operation import atan_norm, min_max_norm
import math

def red_channel(count_vector):
    """Creates the red channel values of the each components of the pixel vector.

    Args:
        count_vector ([int]): The occurrence of numbers in the decimal vector.

    Returns:
        [int]: The red channel values of the each components.
    """
    beta = [math.floor(min_max_norm(atan_norm(count)) * (-255) + 255) for count in count_vector]
    return beta