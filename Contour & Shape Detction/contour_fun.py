import cv2

img = cv2.imread("Contour & Shape Detction/triangle.png")
if img is None:
    raise ValueError("Image not found or could not be loaded")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 250, 300, cv2.THRESH_BINARY)

# FIND CONTOURS : (contours, heirarchy) = cv2.findContours(image, mode, method)
contours, heirarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# DRAW CONTOURS :  cv2.drawContours(image, contours, contourIdx, color, thickness)
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for contour in contours:
    # it will give us the corner points of the contour
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    # it will give us the x coordinate of the first corner point AND RAVEL will convert the 2D array to 1D array
    x = approx.ravel()[0]
    # it will give us the y coordinate of the first corner point and we are subtracting 10 to move the text above the contour
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x, y),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 1)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
