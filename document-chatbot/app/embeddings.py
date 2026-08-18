from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

def create_vector_store(text):
    """Splits text, creates embeddings, stores in FAISS."""
    # 1. Split text into chunks
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    chunks = splitter.split_text(text)

    # 2. Generate embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 3. Store in FAISS vector DB
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore