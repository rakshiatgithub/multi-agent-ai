from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def planner(query):

    prompt=f"""
You are an expert AI Planner.

For the question:

{query}

Generate:

1. Goal
2. Important keywords
3. Research strategy
4. Expected final output

Respond in markdown.
"""

    return llm.invoke(prompt).content
