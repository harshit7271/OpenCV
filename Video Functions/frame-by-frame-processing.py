# saving the video

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')  # type: ignore
recorded = cv2.VideoWriter("my_video.avi", codec, 20,
                           (frame_width, frame_height))

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read the frame")
        break

    recorded.write(frame)
    cv2.imshow('Recording live', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break

camera.release()
recorded.release()
cv2.destroyAllWindows()
