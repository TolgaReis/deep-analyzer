import math_operation
import numpy as np

def create_decimal_vector(filename):
    """Reads the binary file that is given as parameter and
       converts it to decimal integer list.

    Args:
        filename (string): The name of the file that is read.
    """

    vector = list()
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read(1)
        while binary_data != b'':
            vector.append(ord(binary_data))
            binary_data = binary_file.read(1)
    return vector

def create_count_vector(vector):
    """Constructs a count vector based on the occurrence of
       numbers in the decimal vector (byte frequency)

    Args:
        decimal_vector ([int]): 8-bit unsigned integers read
        from the binary.

    Returns:
        [int]: Byte frequency vector.
    """

    return [vector.count(byte) for byte in range(0, 256)]

def create_pixel_vector(count_vector, decimal_vector):
    """Takes count and decimal vectors, then returns the pixel vector.

    Args:
        count_vector ([int]): Number of the counts of the bytes.
        decimal_vector ([type]): Vector of the bytes in file.

    Returns:
        np.array: RGB pixel vector as np.array type.
    """
    pixel_vector = np.array([decimal_vector, [count_vector[byte] for byte in decimal_vector], [0 for byte in decimal_vector]])
    
    return pixel_vector