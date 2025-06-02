from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
client = QdrantClient(path="./model/db")


from langchain.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain.vectorstores import Qdrant as QdrantVectorStore

# # ✅ Step 1: Create embedding wrapper
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# from sentence_transformers import SentenceTransformer

# embeddings = SentenceTransformer("all-MiniLM-L6-v2")


# # ✅ Step 3: Create collection (make sure size matches 384)
# client.recreate_collection(
#     collection_name="demo_collection",
#     vectors_config=VectorParams(size=384, distance=Distance.COSINE),
# )

# # ✅ Step 4: Initialize vector store
# vector_store = QdrantVectorStore(
#     client=client,
#     collection_name="demo_collection",
#     embedding=embeddings
# )


vector_store = QdrantVectorStore(
    client=client,
    collection_name="demo_collection",
    embeddings=embeddings,
)

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS  # or Chroma, etc.
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

# Sample list of PDF file paths
pdf_files = ["Generative_AI_Enterprise_Strategy.pdf"]

# Recursive splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

all_documents = []

for pdf_file in pdf_files:
    loader = PyPDFLoader(pdf_file)
    pages = loader.load()

    # Split and add source metadata
    for page in pages:
        chunks = text_splitter.split_documents([page])
        for chunk in chunks:
            chunk.metadata["source"] = os.path.basename(pdf_file)
        all_documents.extend(chunks)


# Add all documents to the vector store
vector_store.add_documents(documents=all_documents)
