import math_operation
import numpy as np
from config import Config
from PIL import Image

def save_image(pixel_vector, data_type, filename):
    """Saves image to malware or benign data directory according to parameter.

    Args:
        pixel_vector (np.array): Numpy array that holds the pixels of the image.
        data_type (str): Provides the data type information to save image right
                         directory.
        filename (str): Used to save image with prior file name.

    Raises:
        Exception: If the file type invalid, then raises exception.
    """
    img = Image.fromarray(pixel_vector, 'RGB')
    img = img.resize((512, 512))

    if data_type in Config.DATA_TYPES:
        img.save(Config.DATA_DIR % (data_type, filename))
    else:
        raise Exception

def create_vectors(filename):
    """Reads the binary file that is given as parameter and
       converts it to decimal integer list.

    Args:
        filename (string): The name of the file that is read.
    """
    decimal_vector = list()
    count_vector = [0] * (Config.MAX_UNSIGNED_BYTE_VAL + 1)
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read(1)
        while binary_data != b'':
            decimal_data = ord(binary_data)
            decimal_vector.append(decimal_data)
            count_vector[decimal_data] += 1
            binary_data = binary_file.read(1)

    return decimal_vector, count_vector

def create_pixel_vector(file):
    """Takes count and decimal vectors, then returns the pixel vector.

    Args:
        count_vector ([int]): Number of the counts of the bytes.
        decimal_vector ([type]): Vector of the bytes in file.

    Returns:
        np.array: RGB pixel vector as np.array type.
    """
    count_vector, decimal_vector = create_vectors(file)

    count_vector = [math_operation.atan_norm(element) for element in count_vector]
    min_value = min(count_vector)
    max_value = max(count_vector)
    count_vector = [math_operation.beta(element, min_value, max_value) for element in count_vector]

    red_channel = decimal_vector
    green_channel = [0] * len(decimal_vector)
    blue_channel = [count_vector[element] for element in decimal_vector]

    pixel_vector = np.array([red_channel, green_channel, blue_channel])

    return pixel_vector
