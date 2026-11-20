import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Set your API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Você é um atendente de uma pizzaria chamada Pizza do Michael. Seu atendimento é descontraído e simpático. Apresente-se em duas frases."
)

# Print the generated content
print(response.text)