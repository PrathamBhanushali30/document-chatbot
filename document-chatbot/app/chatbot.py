from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def get_chatbot(vectorstore):
    """Creates chatbot pipeline using Retrieval-Augmented Generation (RAG) offline with local model."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Load FLAN-T5 locally (small is faster, base/large need more RAM)
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",   # You can try flan-t5-base if your PC has enough memory (8GB+)
        tokenizer="google/flan-t5-small"
    )

    llm = HuggingFacePipeline(pipeline=generator)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa