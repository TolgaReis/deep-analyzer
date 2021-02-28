from math_operation import atan_norm, min_max_norm
from config import Config
import math

def red_channel(count_vector):
    """Creates the red channel values of the each components of the pixel vector.

    Args:
        count_vector ([int]): The occurrence of numbers in the decimal vector.

    Returns:
        [int]: The red channel values of the each components.
    """
    red_channel_list = list()
    minimum = min(count_vector)
    maximum = max(count_vector)
    
    for count in count_vector:
        norm = min_max_norm(atan_norm(count), minimum, maximum)
        beta = math.floor(norm * (-Config.MAX_UNSIGNED_BYTE_VAL) + Config.MAX_UNSIGNED_BYTE_VAL)
        red_channel_list.append(beta)

    return red_channel_list