import cv2

image = cv2.imread("colouredTurtle copy.png", cv2.IMREAD_GRAYSCALE)

# cv2.threshold(src, t1, t2, method)
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("thresholded image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
90-0 black
130-255 white
180-255 white
50-0 black
"""
