# from google import genai
# from dotenv import load_dotenv
# import os

# # โหลด .env
# load_dotenv()

# # สร้าง client โดยระบุ key ให้ชัด
# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
# )

# print(response.text)
import cv2

cap = cv2.VideoCapture(0)  # 0 = กล้องตัวแรก

if not cap.isOpened():
    print("❌ เปิดกล้องไม่ได้")
    exit()

print("📷 กล้องพร้อม กด SPACE เพื่อถ่าย / ESC เพื่อออก")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Photobooth Camera", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break
    elif key == 32:  # SPACE
        cv2.imwrite("output/photo.jpg", frame)
        print("✅ ถ่ายรูปแล้ว → output/photo.jpg")
        break

cap.release()
cv2.destroyAllWindows()