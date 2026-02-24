# import cv2
# import time

# def capture_after_countdown(cap, seconds=5):
#     start = time.time()
#     while True:
#         ret, frame = cap.read()
#         remaining = seconds - int(time.time() - start)

#         if remaining <= 0:
#             return frame

#         cv2.putText(
#             frame,
#             f"Capture in {remaining}",
#             (50, 100),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             2,
#             (0, 0, 255),
#             3
#         )

#         cv2.imshow("AI Photobooth", frame)
#         cv2.waitKey(1)

# app/camera.py

def capture_image():
    """Return a path to a captured image.

    Behavior:
    - If `output/photo.jpg` exists (from a previous capture), copy it to
      `input/user.jpg` and return that path.
    - Otherwise create `input/user.png` (1x1 placeholder) and return that path.

    This keeps `test.py` runnable on machines without a camera.
    """
    import os
    import shutil
    import base64

    out_photo = os.path.join("output", "photo.jpg")
    inp_dir = "input"
    os.makedirs(inp_dir, exist_ok=True)

    if os.path.exists(out_photo):
        dst = os.path.join(inp_dir, "user.jpg")
        try:
            shutil.copyfile(out_photo, dst)
            return dst
        except Exception:
            # fall through to creating placeholder
            pass

    # small 1x1 PNG placeholder
    png_b64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMA"
        "ASsJTYQAAAAASUVORK5CYII="
    )
    placeholder = os.path.join(inp_dir, "user.png")
    with open(placeholder, "wb") as f:
        f.write(base64.b64decode(png_b64))

    return placeholder