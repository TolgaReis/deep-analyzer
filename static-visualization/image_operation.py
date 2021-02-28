import os 

def decimal_vector(filename):
    """Reads the binary file that is given as parameter and converts it to decimal integer list. 

    Args:
        filename (string): The name of the file that is read.
    """

    decimal_vector = list()
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read(1)
        while binary_data != b'':
            decimal_vector.append(ord(binary_data))
            binary_data = binary_file.read(1)
    return decimal_vector

def count_vector(decimal_vector):
    """Constructs a count vector based on the occurrence of numbers in the decimal vector (byte frequency)

    Args:
        decimal_vector ([integer]): 8-bit unsigned integers read from the binary.

    Returns:
        [integer]: Byte frequency vector.
    """
    count_vector = [decimal_vector.count(byte) for byte in range(0, 256)]

    return count_vector
