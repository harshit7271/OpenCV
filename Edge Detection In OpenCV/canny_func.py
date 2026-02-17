import cv2

image = cv2.imread("colouredTurtle copy.png", cv2.IMREAD_GRAYSCALE)


# Canny(src, threshold1, threshold2)
edges = cv2.Canny(image, 0, 255)

cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
