import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Could not read image")
else:
    print("Loaded")

#  GaussianBlur(image, (kerner_size_x, kernel_size_y(both in odd num)), sigma)
blurred = cv2.GaussianBlur(image, (5, 5), 0)  # type: ignore

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
