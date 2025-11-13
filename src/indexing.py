import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from document_loader import load_documents, load_from_urls
from text_splitter import split_documents
from vector_store import get_vector_store
from typing import Iterable, Optional


def index_documents(directory_path: str = "data/documents", web_urls: Optional[Iterable[str]] = None) -> int:
    """Ejecuta la pipeline de indexación."""
    print ("=================================================")
    if web_urls:
        documents = load_from_urls(web_urls)
    else:
        documents = load_documents(directory_path)
    print ("=================================================")
    chunks = split_documents(documents)
    print ("=================================================")
    vectorstore = get_vector_store()
    vectorstore.add_documents(chunks)
    print(f"Indexing.py -> {len(chunks)} documentos almacenados en Pinecone.")
    print ("=================================================")
    return len(chunks)

#index_documents(web_urls=["https://lilianweng.github.io/posts/2023-06-23-agent/"])
#index_documents()
