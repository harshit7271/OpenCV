import cv2

# To read the image
flag = cv2.IMREAD_COLOR

image = cv2.imread("colouredTurtle copy.png", flag)

if image is None:
    print("Image not found or failed to load")
else:
    print("Image loaded successfully:", image)


# dimensions
if image is not None:
    h, w, c = image.shape
    print(
        f"Height od image: {h}\nWidth of the image: {w}\nColour channels: {c}")
