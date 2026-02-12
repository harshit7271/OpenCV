import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is not None:
    cv2.imshow("Displaying image ", image)  # opens the window
    cv2.waitKey(0)  # wait for a key
    cv2.destroyAllWindows()  # closes the window
else:
    print("Unable to load the image")
