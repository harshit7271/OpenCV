import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not loaded")
else:
    print("Loaded")

    cv2.putText(image,
                "Kachuwa",  # desired text
                (150, 150),  # co-ordinates
                cv2.FONT_HERSHEY_COMPLEX,  # Font
                1.2,  # Font scale
                (0, 0, 0),  # Font color
                thickness=2)

    cv2.imshow("original image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
