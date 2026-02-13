import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not loaded")
else:
    print("Loaded")

    cv2.circle(image, (250, 170), 150, (0, 255, 0), thickness=-1)

    cv2.imshow("Circle", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
