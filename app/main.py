import cv2
import time
from hand_gesture import HandGesture
from background import BackgroundRemover

cap = cv2.VideoCapture(0)
gesture = HandGesture()
bg_remover = BackgroundRemover()

backgrounds = [
    cv2.imread("backgrounds/beach.jpg"),
    cv2.imread("backgrounds/city.jpg"),
    cv2.imread("backgrounds/studio.jpg")
]
bg_index = 0

countdown = False
countdown_done = False
start_time = 0
captured = None
last_trigger_time = 0
TRIGGER_COOLDOWN = 3  # กัน gesture รัว

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    now = time.time()

    # 🖐️ Detect gesture
    if (
        not countdown
        and not countdown_done
        and gesture.is_two_fingers(rgb)
        and now - last_trigger_time > TRIGGER_COOLDOWN
    ):
        countdown = True
        start_time = now
        last_trigger_time = now

    # ⏱️ Countdown
    if countdown:
        remaining = int(5 - (now - start_time))
        if remaining > 0:
            cv2.putText(
                frame, f"{remaining}",
                (300, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                4, (0, 0, 255), 5
            )
        else:
            captured = frame.copy()
            countdown = False
            countdown_done = True

    # 🧍 Composite background
    if captured is not None:
        output = bg_remover.remove(captured, backgrounds[bg_index])
        cv2.imshow("AI Photobooth", output)
    else:
        cv2.imshow("AI Photobooth", frame)

    key = cv2.waitKey(1) & 0xFF

    # 🔄 เปลี่ยนฉาก
    if key == ord('b'):
        bg_index = (bg_index + 1) % len(backgrounds)

    # 🔁 ถ่ายใหม่
    if key == ord('r'):
        captured = None
        countdown_done = False

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
