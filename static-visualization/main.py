import shutil
import os
import image_operation
from config import Config

def main():
    """[summary]
    """

    benign_file_list = os.listdir(Config.FILES_BENIGN_UNCONVERTED)
    malware_file_list = os.listdir(Config.FILES_MALWARE_UNCONVERTED)

    for file in benign_file_list:
        unconverted_file_path = f'{Config.FILES_BENIGN_UNCONVERTED}/{file}'
        converted_file_path = f'{Config.FILES_BENIGN_CONVERTED}/{file}'

        pixel_vector = image_operation.create_pixel_vector(unconverted_file_path)
        image_operation.save_image(pixel_vector, Config.DATA_TYPES[1], file)
        shutil.move(unconverted_file_path, converted_file_path)

    for file in malware_file_list:
        unconverted_file_path = f'{Config.FILES_MALWARE_UNCONVERTED}/{file}'
        converted_file_path = f'{Config.FILES_MALWARE_CONVERTED}/{file}'

        pixel_vector = image_operation.create_pixel_vector(unconverted_file_path)
        image_operation.save_image(pixel_vector, Config.DATA_TYPES[0], file)
        shutil.move(unconverted_file_path, converted_file_path)

if __name__ == "__main__":
    main()
