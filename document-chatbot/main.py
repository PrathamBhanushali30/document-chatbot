import streamlit as st
from app.utils import extract_text_from_pdf
from app.embeddings import create_vector_store
from app.chatbot import get_chatbot

st.set_page_config(page_title="📘 Document Chatbot")

st.title("📘 Document Chatbot (RAG + LLM)")

# Upload PDF
pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

if pdf_file:
    with st.spinner("Processing document..."):
        # Step 1: Extract text
        text = extract_text_from_pdf(pdf_file)

        # Step 2: Create vector store
        vectorstore = create_vector_store(text)

        # Step 3: Initialize chatbot
        qa = get_chatbot(vectorstore)

    st.success("✅ Document processed! Now ask your questions:")

    # Chat interface
    query = st.text_input("Enter your question here")
    if query:
        with st.spinner("Thinking..."):
            result = qa({"query": query})
            st.write("### 🤖 Answer:")
            st.write(result["result"])

            st.write("### 📖 Source Snippets:")
            for doc in result["source_documents"]:
                st.markdown(f"- {doc.page_content[:200]}...")