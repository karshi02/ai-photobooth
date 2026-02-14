import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection.FaceDetection()

def extract_face(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = mp_face.process(rgb)

    if not result.detections:
        return None

    box = result.detections[0].location_data.relative_bounding_box
    h, w, _ = image.shape

    x1 = int(box.xmin * w)
    y1 = int(box.ymin * h)
    x2 = int((box.xmin + box.width) * w)
    y2 = int((box.ymin + box.height) * h)

    return image[y1:y2, x1:x2]
