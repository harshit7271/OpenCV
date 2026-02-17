"""
- cv2.bitwise_and(img1, img2) : basically it is used remove overlappiong white areas in imgs
or to cut out the image.
- cv2.bitwise_or(img1, img2) : used to merge multiple images into one image.
- cv2.bitwise_not(img) : to rverse the image, ex white to black or black to white, inshort to create effects. Also used in removing background img in apple iphones
"""

import cv2
import numpy as np

# height and width of both the images should be same
# use only black and white image or conver them into gray scale image (using cv2.IMREAD_GRAYSCALE)

image1 = np.zeros((300, 300), dtype="uint8")
image2 = np.zeros((300, 300), dtype="uint8")

# will draw a circle on image 1
cv2.circle(image1, (150, 150), 100, 255, -1)

# will draw a rectangle on image 2
cv2.rectangle(image2, (100, 100), (250, 250), 255, -1)


bitwised1 = cv2.bitwise_and(image1, image2)
bitwised2 = cv2.bitwise_or(image1, image2)
bitwised3 = cv2.bitwise_not(image1)

cv2.imshow("Circle", image1)
cv2.imshow("Rectangle", image2)
cv2.imshow("AND", bitwised1)
cv2.imshow("OR", bitwised2)
cv2.imshow("NOT", bitwised3)

cv2.waitKey(0)
cv2.destroyAllWindows()
