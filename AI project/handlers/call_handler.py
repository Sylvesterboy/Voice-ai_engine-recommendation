from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import os

app = Flask(__name__)

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route("/voice", methods=["POST"])
def handle_call():
    response = VoiceResponse()
    response.say("Hello, this is your AI sales assistant. How can I help you today?")
    response.record(timeout=5, action="/process_audio")
    return str(response)

def make_outbound_call(to_number):
    call = client.calls.create(
        twiml='<Response><Say>Hello! This is your AI assistant.</Say></Response>',
        to=to_number,
        from_=TWILIO_PHONE
    )
    return call.sid

if __name__ == "__main__":
    app.run(port=5000, debug=True)
