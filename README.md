📚 HEC Policy PDF Question Answering System (RAG-based)
This project implements a Retrieval-Augmented Generation (RAG) pipeline to enable intelligent question answering over a collection of 6 Higher Education Commission (HEC) policy documents in PDF format.

It allows users to ask natural language questions and receive accurate, context-aware answers, grounded directly in the official HEC policy books.

🚀 Key Features
Automatic PDF Loading – Extracts and reads all pages from HEC policy documents.

Text Chunking – Breaks down long policy documents into smaller overlapping segments for precise information retrieval.

Semantic Search with FAISS – Stores and retrieves document chunks based on meaning, not keywords.

Question Answering via Mistral AI – Uses the Mistral language model to generate answers with context from HEC policies.

Custom Prompt Design – Ensures answers are well-grounded and avoids hallucinations.

🧱 Components
PDF Loader: Ingests all 6 policy books from a folder.

Chunk Splitter: Divides text into manageable parts (~1000 characters) with overlap.

Embedding Generator: Converts text chunks into vectors using a SentenceTransformer model.

FAISS Vector Store: Efficiently retrieves the most relevant policy chunks for a user’s question.

RAG Pipeline: Combines document retrieval with a generative model to produce detailed answers.

🎯 Use Case
This system is designed for:

Students, researchers, or administrators who need quick, reliable answers about HEC policies.

Automating support over large policy documents that are difficult to search manually.

🔐 Requirements
Python 3.8+

LangChain, FAISS, HuggingFace Transformers, Mistral AI (API access)

📝 How It Works (Flow)
Load HEC PDFs from a folder.

Split pages into text chunks.

Generate vector embeddings.

Save all vectors in a FAISS index.

Accept a user query.

Retrieve matching chunks.

Pass context to Mistral LLM for final answer generation.

📄 Documents
The system is built on 6 official HEC policy PDFs:

📌 Notes
Make sure your Mistral API key is active and properly set.

For best results, use well-formatted, searchable PDFs.

Can be extended to other universities or policy domains.
