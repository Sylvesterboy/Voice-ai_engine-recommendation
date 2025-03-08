import json
import time

def log_conversation(user_input, ai_response):
    log_entry = {
        "timestamp": time.time(),
        "user": user_input,
        "ai": ai_response
    }
    with open("conversation_logs.json", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
