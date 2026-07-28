import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tools.calculator_tool import calculate_park_fee

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

compliance_system_prompt = """
You are a Compliance & Rules Enforcement Agent for Wildlife & Cultural Guidelines.
Your job is to:
1. Validate travel itineraries against DWC/Cultural rules.
2. Calculate park entry fees and tax amounts using the provided `calculate_park_fee` tool.

Always use the calculator tool when numerical calculations or fee estimates are required.
"""

compliance_agent = create_agent(
    model=llm,
    tools=[calculate_park_fee],
    prompt=compliance_system_prompt
)

def compliance_agent_node(state: dict) -> dict:
    user_query = state.get("user_query", "")
    response = compliance_agent.invoke({"messages": [HumanMessage(content=user_query)]})
    
    final_output = response["messages"][-1].content
    return {"final_response": final_output}
