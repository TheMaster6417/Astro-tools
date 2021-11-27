
import cv2 as cv
import sys
import tqdm

image = sys.argv
def star_detection(image): #based on https://github.com/TheMaster6417/StarRemoval/blob/main/starFunctions.py
    cv.imread(image)
    cv.imshow(image)

star_detection(image)