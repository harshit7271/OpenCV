import cv2


img = cv2.imread("Contour & Shape Detction/triangle.png")
if img is None:
    raise ValueError("Image not found or could not be loaded")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 250, 300, cv2.THRESH_BINARY)


# FIND CONTOURS : (contours, heirarchy) = cv2.findContours(image, mode, method)


contours, heirarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# DRAW CONTOURS :  cv2.drawContours(image, contours, contourIdx, color, thickness)
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
