
import os
from dotenv import load_dotenv
from google import genai

print("Starting Gemini API program...")

# Load API key from .env
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

print("API key loaded successfully!")
print("Connecting to Gemini...")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Make first LLM API call
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Display the response
print("\nLLM Response:")
print(response.text)
