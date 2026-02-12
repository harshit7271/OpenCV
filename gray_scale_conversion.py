# By converting into gray format we reduce processing time and complexity

import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is not None:
    # conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # display
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save
    cv2.imwrite("gray_scale.png", gray)
else:
    print("Unable to load")
