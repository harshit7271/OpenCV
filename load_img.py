import cv2

# To read the image
flag = cv2.IMREAD_COLOR

image = ("colouredTurtle copy.png", flag)

if image is None:
    print("Image not found or failed to load")
else:
    print("Image loaded successfully:", image)
