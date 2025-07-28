# rag_query.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_mistralai.chat_models import ChatMistralAI
import os
import warnings
warnings.filterwarnings("ignore")


# ✅ 1. Load vector store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

# ✅ 2. Set Mistral API key
os.environ["MISTRAL_API_KEY"] = "Your_Mistral_API_Key_Here"  # Replace with your actual Mistral API key

# ✅ 3. Define Mistral model
llm = ChatMistralAI(model="mistral-small")

# ✅ 4. Set up retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})


# ✅ 5. Custom prompt template
template = """
Answer the question based on the provided context. If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# ✅ 6. Build RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

# ✅ 7. Ask questions
while True:
    query = input("\n🧠 Ask a question (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    result = qa_chain(query)
    print("\n💬 Answer:\n", result["result"])
