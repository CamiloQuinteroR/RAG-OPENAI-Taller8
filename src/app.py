from rag_chain import ask
from indexing import index_documents

def main():
    """Loop principal de la aplicación.

    El usuario escribe preguntas por consola: al escribir `salir` se termina el
    programa. Cada pregunta se pasa a `ask()` para procesar y mostrar la
    respuesta:
    """
    print("===================================================")
    print("RAG con LangChain, Pinecone y OpenAI")
    print("===================================================")
    while True:
        query = input("\nPregunta lo que quieras... (o 'exit'): ")
        if query.lower() in ["exit"]:
            break
        ask(query)


if __name__ == "__main__":
    index_documents(web_urls=["https://lilianweng.github.io/posts/2023-06-23-agent/"])
    main()
