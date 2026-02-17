import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Could not read image")
else:
    print("Loaded")

blurred = cv2.medianBlur(image, 11)  # type: ignore

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.imwrite("turtle.png", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
