import image_operation
import os
from config import Config

def main():
    """[summary]
    """
    owd = os.getcwd()
    os.chdir(Config.FILES_BENIGN)
    for file in os.listdir():
        decimal_vector, count_vector = image_operation.create_vectors(file)
        pixel_vector = image_operation.create_pixel_vector(count_vector, decimal_vector)
        os.chdir(owd)
        image_operation.save_image(pixel_vector, Config.DATA_TYPES[1], file)

    owd = os.getcwd()
    os.chdir(Config.FILES_BENIGN)
    for file in os.listdir():
        decimal_vector, count_vector = image_operation.create_vectors(file)
        pixel_vector = image_operation.create_pixel_vector(count_vector, decimal_vector)
        os.chdir(owd)
        image_operation.save_image(pixel_vector, Config.DATA_TYPES[0], file)

if __name__ == "__main__":
    main()
