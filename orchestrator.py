from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

from agents.router_agent import router_classifier_node
from agents.retriever_agent import retriever_agent_node
from agents.compliance_agent import compliance_agent_node

class AgentState(TypedDict):
    user_query: str
    next_step: str
    final_response: str

def route_decision(state: AgentState) -> Literal["compliance_node", "retriever_node"]:
    if state["next_step"] == "compliance":
        return "compliance_node"
    return "retriever_node"

workflow = StateGraph(AgentState)

workflow.add_node("router", router_classifier_node)
workflow.add_node("compliance_node", compliance_agent_node)
workflow.add_node("retriever_node", retriever_agent_node)

workflow.set_entry_point("router")
workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "compliance_node": "compliance_node",
        "retriever_node": "retriever_node"
    }
)

workflow.add_edge("compliance_node", END)
workflow.add_edge("retriever_node", END)

orchestrator_app = workflow.compile()
