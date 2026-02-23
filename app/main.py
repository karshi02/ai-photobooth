from google import genai
from dotenv import load_dotenv
import os
from ai.agent import PhotoboothAgent
from camera.capture import capture_photo
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
agent = PhotoboothAgent(client)

print("🤖 AI:", agent.say("Say hello and tell the user to get ready"))

time.sleep(2)
print("🤖 AI: 3")
time.sleep(1)
print("🤖 AI: 2")
time.sleep(1)
print("🤖 AI: 1")

if capture_photo():
    print("📸 ถ่ายรูปเสร็จแล้ว!")
    print("🤖 AI:", agent.say("React happily to a photo being taken"))