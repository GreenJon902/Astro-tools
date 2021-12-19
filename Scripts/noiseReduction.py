from typing import Union, IO, Optional

import numpy as np


def remove_noise(img_in: Union[str, IO, np.ndarray], img_out: Union[str, IO] = None) -> Optional[np.ndarray]:
    """
    A function to remove noise from an image

    :param img_in: The image that will have noise removed from
    :param img_out: The final image (none if you just want the np.ndarray and don't want to write to a file)
    :return:
    """


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:  # 3 because of path
        print("noiseReduction.py requires two arguments!")
        sys.exit()

    file = sys.argv[1]
    out = sys.argv[2]
