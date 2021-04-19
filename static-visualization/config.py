class Config:
    """Used for general configuration values.
    """
    MAX_UNSIGNED_BYTE_VAL = 255

    DATA_TYPES = ['malware', 'benign']
    DATA_DIR = '../data/%s/unloaded/%s.jpeg'

    FILES_BENIGN_UNCONVERTED = '../files/benign/unconverted'
    FILES_BENIGN_CONVERTED = '../files/benign/converted'

    FILES_MALWARE_UNCONVERTED = '../files/malware/unconverted'
    FILES_MALWARE_CONVERTED = '../files/malware/converted'
    