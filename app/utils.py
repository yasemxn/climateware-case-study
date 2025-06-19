import os
import openai
from dotenv import load_dotenv

load_dotenv()

# API and Azure settings
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_API_VERSION")

DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# Ask GPT Function
def ask_gpt(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            engine=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in carbon emission reduction strategies."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error calling GPT: {e}"
