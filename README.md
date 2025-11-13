
# 🧠 RAG con LangChain, OpenAI y Pinecone

Este proyecto implementa un **sistema de Recuperación Aumentada por Generación (RAG)** utilizando **LangChain**, **OpenAI GPT** y **Pinecone**.  
El sistema permite responder preguntas fundamentadas en el contenido de documentos o páginas web mediante la integración de embeddings, recuperación semántica y generación de lenguaje natural.

En este reposositorio se encuentra un proyeco organizado en varios archivos .py, cada uno de estos archivos representa una parte fundamental para el desarollo de nuestro RAG como veremos mas adeltante, así mismo, podemos encontrar dos archivos jupyter, el primer archivo relevante es Guia.ipynb, este archivo contiene la explicación del tutorial que se encuentra en este link https://python.langchain.com/docs/tutorials/llm_chain/, allí logramos familiarizarnos con los conceptos báicos de LangChain siguiendo el tutorial, esto nos proporcionó los conocimientos necesarios para desarrollar neustro agente. El segundo archivo, RAG-OPENAI-PINECONE.ipynb, contiene la misma aplicación de nuestro proyecto pero esta vez, organizado y explicado en el notebook para entender el flujo del agente RAG usando OpenAI y Pinecone. 

---

## ⚙️ Arquitectura del Proyecto

La arquitectura del sistema RAG está compuesta por los siguientes módulos:

1. **Carga de documentos:**  
   Se obtienen los textos desde URLs o archivos locales y se limpian usando `BeautifulSoup`.

2. **División de texto (Chunking):**  
   Se fragmenta el texto con `RecursiveCharacterTextSplitter` para optimizar la recuperación semántica.

3. **Generación de embeddings:**  
   Cada fragmento se convierte en un vector mediante `OpenAIEmbeddings`.

4. **Almacenamiento vectorial:**  
   Los embeddings se indexan en **Pinecone**, que permite realizar búsquedas por similitud.

5. **Recuperación y construcción de contexto:**  
   LangChain busca los fragmentos más relevantes con respecto a la consulta del usuario.

6. **Generación de respuesta (RAG):**  
   Se utiliza el modelo **GPT-4-turbo** de OpenAI para generar una respuesta enriquecida con el contexto recuperado.


---

## 🧩 Componentes Principales

| Componente                         | Descripción                                                         |
| ---------------------------------- | ------------------------------------------------------------------- |
| **LangChain**                      | Framework principal para construir el flujo RAG.                    |
| **OpenAI GPT-4-turbo**             | Modelo de lenguaje que genera respuestas fundamentadas en contexto. |
| **OpenAIEmbeddings**               | Genera representaciones vectoriales de los fragmentos de texto.     |
| **Pinecone**                       | Base de datos vectorial para búsquedas semánticas.                  |
| **BeautifulSoup (bs4)**            | Limpieza y extracción de texto desde HTML.                          |
| **RecursiveCharacterTextSplitter** | Divide el texto en fragmentos para el embedding.                    |

---

## 🧰 Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/Taller-LangChain-LLM.git
cd Taller-LangChain-LLM
```

---

### 2️⃣ Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv .venv
.venv\Scripts\activate   # En Windows
# source .venv/bin/activate   # En macOS o Linux
```

---

### 3️⃣ Instalar dependencias

```bash
pip install langchain openai pinecone-client langchain-community langchain-text-splitters beautifulsoup4
```

---

### 4️⃣ Configurar variables de entorno

Creamos un archivo `.env` en la raíz del proyecto con tus claves:

```bash
OPENAI_API_KEY=""
PINECONE_API_KEY=""
PINECONE_ENVIRONMENT=""
```


---

## 🚀 Ejecución del Proyecto

Tenemos dos opciones:

1. El proyecto se ejecuta directamente en el notebook `RAG-OPENAI-PINECONE-ipynb`.

### Pasos dentro del notebook:

1. **Instalar dependencias** (primera celda).
2. **Configurar las API keys** (segunda celda).
3. **Cargar el documento** desde una URL (ejemplo: blog de Lilian Weng).
4. **Generar embeddings** e indexarlos en Pinecone.
5. **Consultar el sistema** con una pregunta en lenguaje natural.

---
2. Podemos ejecutar el proyecto con los archivos .py, para esto seguiremos los siguientes comandos:

```bash
python src/app.py
```
Esto desde la raiz del proyecto.

---

## 🧪 Ejemplo de Ejecución

1. Para el proyecto ejecutando desde consola app.py:

**Consulta:**

<img width="405" height="40" alt="image" src="https://github.com/user-attachments/assets/39ffcd7a-3629-4a96-8468-76b2cb96769f" />


```text
Que es la ia?
```

**Respuesta generada:**

<img width="836" height="74" alt="image" src="https://github.com/user-attachments/assets/c99b6c44-7c8b-4a09-a75f-e139206e1c63" />

```text
La inteligencia artificial (IA) consiste en enseñar a las máquinas a realizar tareas que normalmente requieren inteligencia humana, como aprender, adaptarse y crear. Esto incluye comprender el lenguaje, analizar datos y generar sugerencias útiles. La IA combina diversas disciplinas, como informática, análisis de datos, estadística, neurociencia, lingüística y filosofía. Un ejemplo de IA es el reconocimiento óptico de caracteres (OCR), que convierte texto en imágenes en datos estructurados, facilitando la obtención de información valiosa.
```
2. Para el notebook:

**Consulta:**

<img width="495" height="111" alt="image" src="https://github.com/user-attachments/assets/d52fdf68-5ede-44ef-8fde-02c80fbee5e7" />


```text  
What is task decomposition?
```

**Respuesta generada:**

<img width="523" height="367" alt="image" src="https://github.com/user-attachments/assets/e0a67015-2a6a-4285-9fc7-9f030bdcfc92" />


```
--- Respuesta del agente RAG ---

Task decomposition is the process of breaking down a larger task into smaller, more manageable sub-tasks or goals. This can be achieved in several ways:

1. Using large language models (LLMs) with simple prompts, such as asking for "Steps for XYZ" or "What are the subgoals for achieving XYZ?"
2. Employing task-specific instructions, like "Write a story outline" for writing a novel.
3. Incorporating human inputs to guide the decomposition process.

Additionally, there is a distinct approach called LLM+P, which involves using an external classical planner for long-horizon planning. This method utilizes the Planning Domain Definition Language (PDDL) to describe the planning problem, where the LLM translates the problem into PDDL, requests a classical planner to generate a plan, and then translates that plan back into natural language.
Si quieres probar ask() ahora, descomenta la llamada o ejecuta ask("tu pregunta").             
```

---

## 🖼️ Captura de Ejemplo y explicación

Al ejecutar nuestro archivo app.py, podemos ver que se cargan los documentos de referencia, o bien el contenido de cualquier pagina web que le proporcionemos a nuestro programa, en el caos de cargar un docuemento, en este caso Referencias.txt podremos ver la siguiente salida en consola cuando el documento es procesado:

<img width="630" height="151" alt="image" src="https://github.com/user-attachments/assets/ec15a097-04c2-4dec-bc86-14bf0c435960" />


En esta ejecución, el sistema cargó un archivo local desde el equipo y lo procesó como fuente de conocimiento. El pipeline de RAG leyó el documento, lo dividió en 10 fragmentos (chunks) y posteriormente generó los embeddings correspondientes para almacenarlos en la base vectorial Pinecone. Este resultado demuestra que el flujo completo —desde la carga hasta la indexación— funciona correctamente con documentos locales de tamaño reducido.

Mientras que cuando se carga una pagina web como por ejemplo https://lilianweng.github.io/posts/2023-06-23-agent/ vemos lo siguiente:

<img width="625" height="152" alt="image" src="https://github.com/user-attachments/assets/9ae8bc66-9d4d-4ba2-b417-c1b9781369cd" />


En este caso, el sistema utilizó el cargador web para extraer el contenido de una página en línea, procesándolo de la misma forma que un documento local. Debido a que la página contenía más información, el texto se dividió en 63 fragmentos, los cuales fueron convertidos en vectores e indexados en Pinecone. Esta ejecución evidencia que el agente RAG puede integrar y comprender fuentes de datos externas, permitiendo consultas sobre información proveniente directamente de la web.

En los dos casos, el rag funciona correctamente y podremos realizarle preguntas como las siguientes:

<img width="1044" height="90" alt="image" src="https://github.com/user-attachments/assets/16bdbea1-6ffd-48e1-89a3-bac6ec0d05eb" />


<img width="1045" height="274" alt="image" src="https://github.com/user-attachments/assets/7557716a-1cf9-4cef-8c19-8735adbb4aa7" />


<img width="1048" height="340" alt="image" src="https://github.com/user-attachments/assets/82456591-4003-4e22-83f9-e7c043604e05" />


En este caso el agente respondio teniendo en cuenta la pagina web proporcionada de referencia, como podemos ver, funciona de forma correcta. 

---

## 👤 Autor

**Camilo Andrés Quintero Rodríguez**
Proyecto: *Creación de un agente RAG con LangChain, OpenAI y Pinecone*
Escuela Colombiana de Ingeniería Julio Garavito – 2025

