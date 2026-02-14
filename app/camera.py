import cv2
import time

def capture_after_countdown(cap, seconds=5):
    start = time.time()
    while True:
        ret, frame = cap.read()
        remaining = seconds - int(time.time() - start)

        if remaining <= 0:
            return frame

        cv2.putText(
            frame,
            f"Capture in {remaining}",
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 0, 255),
            3
        )

        cv2.imshow("AI Photobooth", frame)
        cv2.waitKey(1)
