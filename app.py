import streamlit as st
from agents.router_agent import orchestrator_app

st.set_page_config(page_title="AI Agent Orchestration System", page_icon="🤖")

st.title("🌿 DWC & Cultural Travel AI Assistant")
st.caption("Powered by LangGraph Multi-Agent Architecture")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about park rules, general details, or calculate entrance fees..."):
    
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Agent is routing and processing your request..."):
            initial_state = {"user_query": prompt}
            result = orchestrator_app.invoke(initial_state)
            response_text = result.get("final_response", "Sorry, I couldn't process that.")
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
