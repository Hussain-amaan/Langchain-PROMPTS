from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ updated model
    temperature=0.8
)
response = model.invoke("Write a 5 line poem on cricket")

print(response.content)