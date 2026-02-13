import cv2

image = cv2.imread("colouredTurtle copy.png")

if image is None:
    print("Image not found bhai")

else:
    (h, w) = image.shape[:2]
    centre = (w//2, h//2)

    M = cv2.getRotationMatrix2D(centre, 45, 0.5)   # (centre, angle, scale)
    rotated_img = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original image", image)
    cv2.imshow("Rotated image", rotated_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
