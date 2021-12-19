from typing import Union, IO, Optional

import cv2
import numpy as np


def _remove_noise(image: np.ndarray) -> np.ndarray:
    """
    :param image: A single channel of an image (a greyscale image)
    :return:
    """


def remove_noise(img_in: Union[str, IO, np.ndarray], img_out: Union[str, IO] = None) -> Optional[np.ndarray]:
    """
    A function to remove noise from an image

    :param img_in: The image that will have noise removed from
    :param img_out: The final image (none if you just want the np.ndarray and don't want to write to a file)
    :return:
    """

    image: np.ndarray
    if isinstance(img_in, np.ndarray):
        image = img_in
    elif isinstance(img_in, str):
        image = cv2.imread(img_in)
    elif isinstance(img_in, IO):
        img_in.seek(0)
        img_in_bytes = np.asarray(bytearray(img_in.read()), dtype=np.uint8)
        image = cv2.imdecode(img_in_bytes, cv2.IMREAD_COLOR)
    else:
        raise ValueError(f"Argument img_in from remove_noise needs to be a string, IO object or numpy array, not "
                         f"{type(img_in)}")

    b, g, r = cv2.split(image)
    noise_removed_image = cv2.merge((_remove_noise(b), _remove_noise(g), _remove_noise(r)))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:  # 3 because of path
        print("noiseReduction.py requires two arguments!")
        sys.exit()

    file = sys.argv[1]
    out = sys.argv[2]

    remove_noise(file, out)
