import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import tool

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.load_local("vectorstore_db", embeddings, allow_dangerous_deserialization=True)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

@tool
def search_ecotourism_knowledge_base(query: str) -> str:
    """Sri Lanka eco-tourism details, guidelines, and attractions ---- Use this tool."""
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant information found."
    return "\n\n".join([doc.page_content for doc in docs])
