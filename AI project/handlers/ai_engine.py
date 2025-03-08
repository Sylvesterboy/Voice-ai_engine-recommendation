import openai
import os

openai.api_key = os.getenv("c9c8c93e95111c77e6d29f3c69785d65c5646716")

def generate_response(user_input, conversation_history):
    messages = [{"role": "system", "content": "You are an AI sales agent."}]
    messages += [{"role": "user", "content": text} for text in conversation_history]
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]
