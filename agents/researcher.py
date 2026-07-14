from tools.retriever import get_retriever
from langchain_community.chat_models import ChatOllama

retriever = get_retriever()

llm = ChatOllama(model="llama3")

def researcher(query, plan):

    docs = retriever.invoke(query)

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    prompt=f"""
You are an AI Research Agent.

Research Plan:

{plan}

Retrieved Documents:

{context}

Answer the user's question using only the retrieved context.
"""

    return llm.invoke(prompt).content
