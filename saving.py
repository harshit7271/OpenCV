import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is not None:
    success = cv2.imwrite("output_turtle.png", image)
else:
    print("unexpected error occured")
