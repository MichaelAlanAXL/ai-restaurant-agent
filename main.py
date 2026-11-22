import os
from menu import consultar_cardapio
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Set your API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=[consultar_cardapio]
    )
)

response = chat.send_message(
    "Quanto custa uma pizza de calabresa?"
)

print(response.text)

response = chat.send_message(
    "E uma coca-cola 2L?"
)

print(response.text)