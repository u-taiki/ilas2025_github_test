import os
from dotenv import load_dotenv
import chatgpt

load_dotenv(".env")
chatbot = chatgpt.ChatBot(api_key = os.environ.get("OPENAI_API_KEY"))
print("This program helps you to identify from which country you received phone call.")
while True:
    phone_number = input("Please input phone number: ").strip()
    prompt = phone_number + "はどこの国の電話番号なのか教えてください"
    message = chatbot.chat(prompt)
    print(message)