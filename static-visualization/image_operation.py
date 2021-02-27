import os 

def read_bin(filename):
    """Reads the binary file that is given as parameter and converts it to list. 

    Args:
        filename (string): The name of the file that is read.
    """

    byte_list = list()
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read(1)
        while binary_data != b'':
            byte_list.append(ord(binary_data))
            binary_data = binary_file.read(1)
    return byte_list