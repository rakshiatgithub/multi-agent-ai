from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

def critic(content):
    response = llm.invoke(f"Check this answer for correctness and improve it:\n{content}")
    return response.content