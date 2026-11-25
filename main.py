import os
from menu import consultar_cardapio
from cart import adicionar_item, carrinho, listar_carrinho
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
        system_instruction="""
            Você é um atendente de restaurante. 
            Seja sempre objetivo e não faça perguntas desnecessárias. 
            Não mostre o carrinho automaticamente após adicionar produtos, 
            a menos que o cliente peça para vê-lo.
        """,
        tools=[
            consultar_cardapio, 
            adicionar_item,
            listar_carrinho
        ]
    )
)

# Check menu availability
response = chat.send_message(
    "Vocês têm pizza de calabresa e Coca-Cola 2L?"
)
print(response.text)

# Check unavailable product
response = chat.send_message(
    "Vocês tem hambúrguer?"
)
print(response.text)

# Add products to cart
response = chat.send_message(
    "Quero duas pizzas de calabresa e uma Coca-Cola 2L."
)
print(response.text)

# Show shopping cart
response = chat.send_message(
    "Quero ver meu carrinho."
)
print(response.text)