import image_operation
from PIL import Image
import time

def main():
    """[summary]
    """
    decimal_vector, count_vector = image_operation.create_vectors('files/rufus.exe')
    pixel_vector = image_operation.create_pixel_vector(count_vector, decimal_vector)
    img = Image.fromarray(pixel_vector, 'RGB')
    img = img.resize((512, 512))
    img.save('data/benign/rufus.jpeg')

if __name__ == "__main__":
    main()
