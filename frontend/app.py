import streamlit as st
import requests

# --------------------------------------
# App Config
# --------------------------------------
st.set_page_config(
    page_title="RAG Document Assistant",
    layout="centered"
)

st.title("📄 Document Q&A Assistant")
st.caption("Ask questions from your uploaded documents")

BACKEND_URL = "http://127.0.0.1:8000/chat/chat"

# --------------------------------------
# Input Box
# --------------------------------------
query = st.text_input("Ask a question:", placeholder="e.g. What is the policy coverage?")

# --------------------------------------
# Submit Button
# --------------------------------------
if st.button("Ask") and query.strip():

    with st.spinner("Thinking..."):
        response = requests.post(
            BACKEND_URL,
            json={"query": query},
            stream=True
        )

        answer_placeholder = st.empty()
        full_response = ""

        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                text = chunk.decode("utf-8")
                full_response += text
                answer_placeholder.markdown(full_response)

# --------------------------------------
# Footer
# --------------------------------------
st.markdown("---")
st.caption("Powered by Azure OpenAI + RAG")
