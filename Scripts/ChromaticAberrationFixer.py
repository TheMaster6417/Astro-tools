import numpy as np
import cv2
import tqdm
import sys

threshold = 0.2


def star_detection(image):  # based on https://github.com/TheMaster6417/StarRemoval/blob/main/starFunctions.py
    imageG = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('original', image)
    # cv2.imshow('greyscale', imageG)
    template = cv2.imread('../Images/airplanesinthenightskyarelike.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(imageG, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)
    # masking by rotem on stackoverflow
    mask = np.zeros_like(imageG)

    loc2 = list(zip(*loc[::-1]))
    pbar = tqdm.tqdm(len(loc2))
    for pt in loc2:
        # Reduce the size of the rectangle by 3 pixels from each side. old method by rotem
        cv2.circle(mask, (pt[0] + 4, pt[1] + 4), (w - h + 3), 255, -10)  # faster method
        pbar.update(1)
        # use both methods, and it still works/might be better IDK its late ok
    pbar.close()
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    return mask


def remove_dem(mask):
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hsvImage = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
    hsvImageCopy = hsvImage.copy()
    hsvImageCopy = np.float32(hsvImageCopy)
    saturationScale = 2
    H, S, V = cv2.split(hsvImageCopy)

    V = np.clip(V * saturationScale, 0, 255)

    hsvImageCopy = cv2.merge([H, S, V])
    hsvImageCopy = np.uint8(hsvImageCopy)
    hsvImageCopy = cv2.cvtColor(hsvImageCopy, cv2.COLOR_HSV2BGR)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
    cv2.namedWindow("desaturated", cv2.WINDOW_NORMAL)

    # display images
    cv2.imshow("image", mask)
    cv2.imshow("hsv", hsvImage)
    cv2.imshow("desaturated", hsvImageCopy)

    cv2.waitKey(0)


if __name__ == '__main__':
    image = sys.argv[1]
    image = cv2.imread(image)
    image = cv2.resize(image, (800, 800))

    star_mask = star_detection(image)
    remove_dem(star_mask)
