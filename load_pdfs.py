from langchain.document_loaders import PyPDFLoader
import os

# Set the path to your folder containing PDFs
pdf_folder_path = "D:\HEC Rag\documents"

# Collect all PDF files from the folder
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

# Load all documents
documents = []
for file in pdf_files:
    file_path = os.path.join(pdf_folder_path, file)
    loader = PyPDFLoader(file_path)
    documents.extend(loader.load())

# Print total number of pages loaded
print(f"Total documents loaded: {len(documents)}")
print(f"Sample content:\n{documents[0].page_content[:500]}...")
