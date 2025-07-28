from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from split_chunks import chunks  # ensure split_chunks.py returns `chunks`

# Use a good sentence transformer model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create the FAISS vectorstore
vectorstore = FAISS.from_documents(chunks, embedding_model)

# Save locally
vectorstore.save_local("faiss_index")

print("✅ Vectors stored successfully using HuggingFace embeddings.")

vector = embedding_model.embed_query("test")
print(len(vector))  # This is the 'd' FAISS expects
