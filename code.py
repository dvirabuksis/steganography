from PIL import Image
import numpy as np


def encrypt(image: np.ndarray, message: str) -> np.ndarray:
    """
    Encrypt the image with the given message
    Args:
        image: np.ndarray. shape: (N, M)
        message: str.

    Return:
        encrypt_image: np.ndarray. shape: (N, M)
    """
    pass


def decrypt(image: np.ndarray) -> str:
    """
    Decrypt the image and retrive the hidden message
    Args:
        image: np.ndarray. shape: (N, M)

    Return:
        message: str.
    """
    pass


def main():
    
    # TODO: get image from user
    image_url = 'lena.jpg'
    im = np.array(Image.open(image_url))
    
    # break to bytes
    
    
    
    print(im)


if __name__ == "__main__":
    main()