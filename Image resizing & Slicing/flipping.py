import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("image not found")

else:
    print("loaded")

    # flipped vertically, 1 means left to right, -1 means both
    flipped = cv2.flip(image, 1)

    cv2.imshow("Original image", image)
    cv2.imshow("Flipped image", flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
