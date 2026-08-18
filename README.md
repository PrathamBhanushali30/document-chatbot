<div align="center">

# 📄 AI-Powered Document Chatbot

**🤖 Conversational AI • 🧠 Semantic Embeddings • 📑 PDF Processing • ⚡ Fast Retrieval**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![RAG Pipeline](https://img.shields.io/badge/Architecture-RAG-F7931E.svg)](#)
[![NLP](https://img.shields.io/badge/AI-Natural%20Language%20Processing-009688.svg)](#)

An intelligent Retrieval-Augmented Generation (RAG) system designed to parse, embed, and query document data. This chatbot allows users to interact with PDF documents by asking natural language questions, retrieving context-aware answers instantly based on the embedded document content.

<br>

</div>

## 🚀 Overview

Searching through static documents can be a manual and tedious process. This project implements a conversational interface over your data, leveraging modern AI embeddings and Large Language Models (LLMs) to transform how information is extracted and utilized. 

### ✨ Key Features
*   **📑 Intelligent PDF Ingestion:** Processes and extracts text from standard PDF documents. A sample document is provided at `data/test_pdf.pdf` for testing.
*   **🧠 Semantic Embeddings:** Converts extracted text into high-dimensional vector embeddings for rapid semantic search using `app/embeddings.py`.
*   **💬 Context-Aware Chatbot:** Answers user queries accurately by retrieving relevant document chunks and feeding them to an LLM via `app/chatbot.py`.
*   **⚙️ Modular Utilities:** Helper tools and text processing functions are neatly segregated into `app/utils.py`[cite: 2].
*   **🧪 Interactive Experimentation:** Includes a Jupyter notebook (`notebooks/chatbot_refrence_notebook.ipynb`) for prototyping and reference[cite: 2].

---

## 📂 Project Structure

The repository is modular and organized as follows:

*   **`app/chatbot.py`**: Contains the core logic for the conversational interface and LLM integration[cite: 2].
*   **`app/embeddings.py`**: Handles the generation and management of vector embeddings from the parsed text[cite: 2].
*   **`app/utils.py`**: Provides various helper and utility functions for the application[cite: 2].
*   **`data/test_pdf.pdf`**: A sample PDF document included for immediate testing of the pipeline[cite: 2].
*   **`main.py`**: Serves as the primary entry point to launch and orchestrate the application[cite: 2].
*   **`models/`**: A designated directory to house downloaded or locally trained AI models[cite: 2].
*   **`notebooks/chatbot_refrence_notebook.ipynb`**: A Jupyter notebook provided for algorithm reference and exploratory testing[cite: 2].
*   **`requirements.txt`**: Lists all necessary Python dependencies required to run the project[cite: 2].

---

## 🛠️ Quickstart Guide

### 1️⃣ Environment Setup
Clone the repository and set up your virtual environment to isolate dependencies:
```bash
git clone <your-repository-url>
cd document-chatbot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Run the Application
Execute the main script to start processing the sample PDF and initialize the chatbot interface:
```bash
python main.py
```

---

## 🧠 Architecture & Workflow

* 1. Document Ingestion: The system reads the provided PDF files (e.g., `data/test_pdf.pdf`).

* 2. Text Chunking: Text is extracted and split into manageable chunks to optimize context limits for the LLM.

* 3. Vectorization: The `app/embeddings.py` module converts these chunks into semantic vectors, creating a searchable index.

* 4. Retrieval & Generation: When a query is made, `app/chatbot.py` queries the vector store, finds the most relevant document chunks, and synthesizes a precise, context-backed response.


##👨‍💻 Author
Pratham Bhanushali

*M.Tech — Artificial Intelligence & Data Science*

Passionate about bridging the gap between Artificial Intelligence and practical utility, specializing in generative AI workflows, Retrieval-Augmented Generation (RAG), and intelligent automation.
