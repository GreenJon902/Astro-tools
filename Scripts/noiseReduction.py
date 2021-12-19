from typing import Union, IO

import numpy as np


def remove_noise(img_in: Union[str, IO, np.ndarray], img_out: Union[str, IO] = None) -> np.ndarray:
    pass


if __name__ == '__main__':
    import sys

    file = sys.argv[1]
    out = sys.argv[2]
