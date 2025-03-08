import requests
import os

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

def transcribe_audio(audio_url):
    headers = {"Authorization": f"Token {c9c8c93e95111c77e6d29f3c69785d65c5646716}"}
    response = requests.post(
        "https://api.deepgram.com/v1/listen",
        headers=headers,
        json={"url": audio_url}
    )
    return response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
