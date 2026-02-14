# import cv2
# import numpy as np
# import mediapipe as mp

# # ====== Load MediaPipe Selfie Segmentation ======
# mp_selfie = mp.solutions.selfie_segmentation
# segmentor = mp_selfie.SelfieSegmentation(model_selection=1)

# # ====== Load Background Images ======
# bg1 = cv2.imread("backgrounds/beach.jpg")
# bg2 = cv2.imread("backgrounds/space.jpg")

# # ถ้ายังไม่มีภาพ ให้สร้างพื้นสีแทน
# if bg1 is None:
#     bg1 = np.full((720, 1280, 3), (255, 200, 100), dtype=np.uint8)

# if bg2 is None:
#     bg2 = np.full((720, 1280, 3), (50, 50, 255), dtype=np.uint8)

# current_bg = bg1

# # ====== Open Camera ======
# cap = cv2.VideoCapture(0)

# print("Press 1 = Beach")
# print("Press 2 = Space")
# print("Press Q = Quit")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape

#     # Resize background ให้เท่ากล้อง
#     bg_resized = cv2.resize(current_bg, (w, h))

#     # Convert to RGB for MediaPipe
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = segmentor.process(rgb)

#     mask = result.segmentation_mask
#     condition = mask > 0.5

#     # Combine person + background
#     output = np.where(condition[..., None], frame, bg_resized)

#     cv2.imshow("AI Photobooth Demo", output)

#     key = cv2.waitKey(1) & 0xFF

#     if key == ord("1"):
#         current_bg = bg1
#     elif key == ord("2"):
#         current_bg = bg2
#     elif key == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()



import cv2
from hand_gesture import detect_two_fingers
from camera import capture_after_countdown
from face_identity import extract_face
from generator import generate_image

cap = cv2.VideoCapture(0)
captured = False

while True:
    ret, frame = cap.read()
    cv2.imshow("AI Photobooth", frame)

    if detect_two_fingers(frame) and not captured:
        captured = True
        image = capture_after_countdown(cap)
        face = extract_face(image)

        result = generate_image(face)
        cv2.imwrite("../output/result.png", result)
        break

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
