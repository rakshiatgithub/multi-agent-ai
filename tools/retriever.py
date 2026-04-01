from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

def get_retriever():
    loader = TextLoader("data/documents.txt")
    docs = loader.load()

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)

    return db.as_retriever()