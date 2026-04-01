from tools.retriever import get_retriever

retriever = get_retriever()

def researcher(query):
    docs = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in docs])