# # from google import genai
# # from dotenv import load_dotenv
# # import os

# # # โหลด .env
# # load_dotenv()
import time
import os
import sys
import cv2

from app.prompt_builder import build_prompt
from app.pipeline import generate_image


def choose_theme():
	themes = [
		("White Studio / Casual", "white studio", "casual"),
		("Beach / Summer", "tropical beach", "summer"),
		("Dark Studio / Formal", "dark studio", "suit"),
	]

	print("Choose a theme:")
	for i, t in enumerate(themes, start=1):
		print(f"{i}. {t[0]}")

	choice = input("Enter number (default 1): ")
	try:
		idx = int(choice.strip() or "1") - 1
		if idx < 0 or idx >= len(themes):
			idx = 0
	except Exception:
		idx = 0

	return themes[idx][1], themes[idx][2]


def open_camera_and_capture():
	# Try to use mediapipe-based gesture detection if available
	gesture_available = True
	try:
		from app.hand_gesture import detect_two_fingers
	except Exception:
		gesture_available = False

	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		print("❌ Cannot open camera — falling back to placeholder input file")
		# fallback: return any existing input (app.camera.capture_image behavior)
		from app.camera import capture_image
		return capture_image()

	print("Camera opened. Show two fingers or press SPACE to take photo.")

	captured_path = None

	while True:
		ret, frame = cap.read()
		if not ret:
			break

		display = frame.copy()
		h, w = display.shape[:2]
		cv2.putText(display, "Show two fingers or press SPACE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

		cv2.imshow("AI Photobooth - Press ESC to exit", display)

		triggered = False
		if gesture_available:
			try:
				if detect_two_fingers(frame):
					triggered = True
			except Exception:
				gesture_available = False

		key = cv2.waitKey(1) & 0xFF
		if key == 27:  # ESC
			break
		if key == 32:  # SPACE
			triggered = True

		if triggered:
			# Countdown
			for i in range(3, 0, -1):
				ret, frame = cap.read()
				if not ret:
					break
				overlay = frame.copy()
				cv2.putText(overlay, f"Capture in {i}", (w//2 - 80, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 5)
				cv2.imshow("AI Photobooth - Press ESC to exit", overlay)
				cv2.waitKey(1000)

			# final capture
			ret, frame = cap.read()
			if ret:
				os.makedirs("output", exist_ok=True)
				out_path = os.path.join("output", "photo.jpg")
				cv2.imwrite(out_path, frame)
				print("✅ Captured →", out_path)
				captured_path = out_path
			break

	cap.release()
	cv2.destroyAllWindows()

	if captured_path:
		return captured_path
	# fallback
	from app.camera import capture_image
	return capture_image()


def open_file_default(path):
	try:
		if os.name == "nt":
			os.startfile(path)
		else:
			opener = "open" if sys.platform == "darwin" else "xdg-open"
			import subprocess

			subprocess.Popen([opener, path])
	except Exception:
		pass


def main():
	background, outfit = choose_theme()
	print("Selected:", background, outfit)

	print("Opening camera...")
	face_image = open_camera_and_capture()

	# Build prompt and generate
	prompt = build_prompt(background, outfit)
	result = generate_image(prompt)
	print("DONE:", result)

	open_file_default(result)


if __name__ == "__main__":
	main()