"""
R: integration_R (your file may not be called "integration" but whatever it is, the red channel will have the suffix "_R")
G: (integration_B+integration_G)/2
B: ((integration_B+integration_G)/2)*0.85 + integration_R*0.15
https://pixinsight.com/forum/index.php?threads/beginner-need-help-in-processing-hoo.14228/

This is the premise of this HOO preprocessor, made for people without a program with pixelmath functions.
"""

import tifffile
import numpy as np


def HOO(file, out):
    print("Loading Image")
    img = tifffile.imread(file)
    arr = np.array(img)

    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    print("Array converted")
    print("Starting PixelMath")
    arr[:, :, 0] = r
    arr[:, :, 1] = (b + g) / 2
    arr[:, :, 2] = ((b + g) / 2) * 0.85 + r * 0.15
    print("Finished PixelMath")

    tifffile.imsave(f"{out}.tiff", arr)
    print("Finished writing to", out)


if __name__ == "__main__":
    import sys
    HOO(sys.argv[1], sys.argv[2])
