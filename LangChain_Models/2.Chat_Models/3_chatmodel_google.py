from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # loads GOOGLE_API_KEY from your .env

model = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro-latest")

result = model.invoke("What is the capital of India?")
print(result.content)
