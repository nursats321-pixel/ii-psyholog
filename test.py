from google import genai
from dotenv import load_dotenv
import os

load_dotenv("main/.env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:
    message = input("Ты: ")

    if message.lower() == "выход":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message
    )

    print("ИИ:", response.text)