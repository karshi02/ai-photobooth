import cv2
import time

def capture_photo(path="output/photo.jpg"):
    cap = cv2.VideoCapture(0)
    time.sleep(1)

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(path, frame)

    cap.release()
    return ret