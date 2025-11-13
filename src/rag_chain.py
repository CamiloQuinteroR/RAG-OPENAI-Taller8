
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from vector_store import get_vector_store
from config.config import TOP_K


def create_rag_chain():
    """Construye el pipeline RAG usando la API moderna."""
    vectorstore = get_vector_store()
    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_template("""
    Usa el siguiente contexto para responder la pregunta del usuario.
    Si no tienes suficiente información, responde honestamente que no la tienes.

    Contexto:
    {context}

    Pregunta:
    {question}
    """)

    rag_chain = (
        RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
        | prompt
        | llm
    )

    return rag_chain


def ask(question: str):
    """Ejecuta la RAG chain para una pregunta y muestra resultados."""
    rag_chain = create_rag_chain()
    result = rag_chain.invoke(question)

    print("\nRespuesta del RAG: ")
    print(result.content)
