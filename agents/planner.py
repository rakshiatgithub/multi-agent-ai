from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def planner(query):
    response = llm.invoke(f"Break this task into clear steps:\n{query}")
    return response.content