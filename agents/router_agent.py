import os
from typing import TypedDict, Literal
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

class AgentState(TypedDict):
    user_query: str
    next_step: str
    response: str

def router_classifier_node(state: AgentState) -> dict:
    """Classifies user query to determine routing."""
    query = state["user_query"]
    
    prompt = f"""
    Analyze the user request and categorize it into exactly one of these two options:
    - 'compliance': If the query asks about fees, calculations, rules, restrictions, or itinerary validation.
    - 'retriever': If the query asks for general information, park details, history, or guidelines from PDFs.

    Respond with ONLY one word: either 'compliance' or 'retriever'.

    User Request: {query}
    """
    
    response = llm.invoke([HumanMessage(content=prompt)]).content.strip().lower()
    next_step = "compliance" if "compliance" in response else "retriever"
    
    return {"next_step": next_step}

workflow = StateGraph(AgentState)

workflow.add_node("router", router_classifier_node)

workflow.set_entry_point("router")

orchestrator_app = workflow.compile()
