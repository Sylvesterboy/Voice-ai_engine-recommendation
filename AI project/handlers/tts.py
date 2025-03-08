import requests
import os

ELEVENLABS_API_KEY = os.getenv("sk_e198e182050583f53a730424152ce9ffdb130e737484a30c")

def text_to_speech(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    response = requests.post(url, headers=headers, json={"text": text})
    return response.content
