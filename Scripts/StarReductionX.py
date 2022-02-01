import cv2

'''
THIS SCRIPT IS TO BE USED ALONGSIDE STARNETT++ TO REDUCE STARS IN THE IMAGE, IT DOESNT
REMOVE THEM COMPLETLY, IT ITERATIVLY REMOVES STARS TO CLEAN UP AN IMAGE.

'''

img = cv2.imread('../Images/Andromeda.tif')
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Goo", thresh)
cv2.waitKey(0)