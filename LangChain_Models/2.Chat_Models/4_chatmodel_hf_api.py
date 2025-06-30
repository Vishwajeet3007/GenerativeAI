from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_API_TOKEN")

client = InferenceClient(
    model="google/flan-t5-small",
    token=hf_token,
    provider="hf-inference"
)

response = client.text_generation(
    prompt="What is the capital of India?",
    max_new_tokens=50
)

print(response)
