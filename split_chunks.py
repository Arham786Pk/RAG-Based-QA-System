import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# ✅ 1. Load all PDFs from the folder
folder_path = "D:/HEC Rag/documents"

# List all PDF files in the folder
pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".pdf")]

# Load all pages from all PDFs
all_pages = []
for file in pdf_files:
    loader = PyPDFLoader(file)
    pages = loader.load()
    all_pages.extend(pages)

print(f"✅ Total pages loaded from all PDFs: {len(all_pages)}")

# ✅ 2. Split into text chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

chunks = text_splitter.split_documents(all_pages)

# ✅ Output summary
print(f"\n✅ Total chunks created: {len(chunks)}")
print("\n🧩 Sample chunk:\n")
print(chunks[0].page_content)
