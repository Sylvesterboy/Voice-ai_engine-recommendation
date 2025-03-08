from flask import Flask, request, jsonify
from handlers.transcriber import transcribe_audio
from handlers.ai_engine import generate_response
from handlers.tts import text_to_speech
from utils.logger import log_conversation

app = Flask(__name__)

conversation_history = []

@app.route("/process_audio", methods=["POST"])
def process_audio():
    audio_url = request.form.get("RecordingUrl")
    user_text = transcribe_audio(audio_url)
    ai_text = generate_response(user_text, conversation_history)
    conversation_history.append(user_text)
    conversation_history.append(ai_text)
    log_conversation(user_text, ai_text)
    speech_output = text_to_speech(ai_text)

    return speech_output, 200, {"Content-Type": "audio/mpeg"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
