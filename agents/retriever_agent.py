import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def retriever_agent_node(state: dict) -> dict:
    """
    RAG Agent node that retrieves context and generates answers.
    """
    user_query = state.get("user_query", "")
    
    retrieved_context = "Park opening hours: 6:00 AM - 6:00 PM. Best time to visit is early morning."
    
    system_prompt = f"""
    You are a Knowledge Retrieval Specialist for DWC/National Parks.
    Answer the user's query accurately using ONLY the provided context.
    
    Context:
    {retrieved_context}
    """
    
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_query)
    ])
    
    return {"final_response": response.content}
