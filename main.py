from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_client = OpenAI(
    base_url="https://router.huggingface.co/v1",  # route requests through Hugging Face
    api_key=os.getenv("API_KEY"),                # use your Hugging Face token
)


def generate_text_with_conversation(messages, model = "meta-llama/Llama-3.1-8B-Instruct"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content


messages = [{"role": "user", "content": "Indian food recipes"}]

print(generate_text_with_conversation(messages))