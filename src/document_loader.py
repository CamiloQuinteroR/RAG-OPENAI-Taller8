from langchain_community.document_loaders import DirectoryLoader, TextLoader, WebBaseLoader
import bs4


def load_documents(directory_path: str):
    """Carga todos los archivos de texto en `directory_path`.
    """
    loader = DirectoryLoader(
        directory_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}, 
    )
    documents = loader.load()
    print(f"Loader -> Documentos cargados por document_loader.py: {len(documents)}")
    return documents


def load_from_urls(web_paths):
    """Carga una o más páginas web y devuelve `Document` objects.
    """
    if isinstance(web_paths, str):
        web_paths = (web_paths,)

    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    loader = WebBaseLoader(web_paths=web_paths, bs_kwargs={"parse_only": bs4_strainer})
    documents = loader.load()
    print(f"Loader -> Documentos web cargados por document_loader.py: {len(documents)}")
    return documents
