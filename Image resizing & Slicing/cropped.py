import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not found")
else:
    print("Loaded image")
    # cropping img into (100,100)
    cropped_img = image[100:300, 100:300]

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(image.shape)
    print(cropped_img.shape)
