from google import genai

class PhotoboothAgent:
    def __init__(self, client):
        self.client = client

    def say(self, text):
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=text
        )
        return response.text.lower()