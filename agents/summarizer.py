from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

def summarizer(content):
    response = llm.invoke(f"Summarize this into a clear, final answer:\n{content}")
    return response.content