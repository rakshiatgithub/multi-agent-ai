from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

def summarizer(content):

    prompt=f"""
You are the Final AI Agent.

Create a polished response.

Include

- Direct answer
- Key points
- Conclusion

Make it professional.
"""

    return llm.invoke(prompt + content).content
