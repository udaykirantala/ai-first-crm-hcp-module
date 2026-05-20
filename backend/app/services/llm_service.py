from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="gemma2-9b-it",
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_llm(prompt: str):

    response = llm.invoke(prompt)

    return response.content