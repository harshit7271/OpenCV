import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not found")
else:
    print("loaded")

    resized = cv2.resize(image, (400, 300))   # (height, width)

    cv2.imshow("Original image", image)
    cv2.imshow("Resized image", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
