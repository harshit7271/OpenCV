import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not loaded")
else:
    print("Loaded")

    pt1 = (70, 200)
    pt2 = (300, 50)

    color = (0, 0, 255)

    cv2.line(image, pt1, pt2, color, thickness=2)

    cv2.imshow("original image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
