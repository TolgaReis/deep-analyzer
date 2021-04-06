import image_operation
from PIL import Image
import time

def main():
    """[summary]
    """
    # FIXME: Approximately 400KB data can be converted to image in 1 sec.
    #        This amound of data is too low. It has to be increased!
    start = time.time()
    print("Start time...")
    decimal_vector = image_operation.create_decimal_vector('files/rufus.exe')
    count_vector = image_operation.create_count_vector(decimal_vector)
    pixel_vector = image_operation.create_pixel_vector(count_vector, decimal_vector)

    img = Image.fromarray(pixel_vector, 'RGB')
    img = img.resize((512, 512))
    img.save('data/benign/rufus.jpeg')
    end = time.time()
    print(f"TOTAL TIME: {end - start} seconds...")

if __name__ == "__main__":
    main()
