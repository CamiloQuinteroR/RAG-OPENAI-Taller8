from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):
        """Divide una lista de `Document` en chunks más pequeños.
        """
        splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                add_start_index=True
        )
        splits = splitter.split_documents(documents)
        print(f"Split -> Total de chunks generados: {len(splits)}")
        return splits
