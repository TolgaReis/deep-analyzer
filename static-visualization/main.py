import visualization
import image_operation
import numpy as np 
import math_operation
from PIL import Image

def main():
    decimal_vector = image_operation.create_decimal_vector('files/rufus.exe')
    count_vector = image_operation.create_count_vector(decimal_vector)

    pixel_vector = image_operation.create_pixel_vector(count_vector, decimal_vector)   

    img = Image.fromarray(pixel_vector, 'RGB')
    img = img.resize((512, 512))
    img.save('data/benign/rufus.jpeg')

if __name__ == "__main__":
    main()
