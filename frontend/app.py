import streamlit as st
import requests
from util.logger import logger

# ------------------------------
# Config
# ------------------------------
BACKEND_URL = "http://localhost:8000/chat/chat"

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🤖",
    layout="centered"
)

logger.INFO("Starting RAG frontend")

st.title("📄 Document Q&A Assistant")
st.caption("Ask questions from your uploaded documents")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
query = st.chat_input("Ask a question about your document...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                BACKEND_URL,
                json={"query": query}
            )

            data = response.json()

            answer = data.get("answer", "No answer found.")
            sources = data.get("sources", [])

            st.markdown(answer)

            if sources:
                st.markdown("---")
                st.caption("Sources:")
                for s in sources:
                    st.markdown(f"- **{s['source']}** (page {s['page']})")

    # Save to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
