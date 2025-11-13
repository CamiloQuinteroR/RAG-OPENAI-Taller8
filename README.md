

# 🧠 RAG con LangChain y Gemini 2.5

Este proyecto implementa un **sistema de Recuperación Aumentada por Generación (RAG)** usando **LangChain** y el modelo **Gemini 2.5** de Google.
El objetivo es demostrar cómo integrar herramientas de recuperación de contexto, embeddings y agentes inteligentes para responder preguntas basadas en documentos locales.

---

## ⚙️ Arquitectura del Proyecto

La arquitectura del sistema está compuesta por los siguientes elementos:

1. **Carga de documentos:**
   Se leen archivos o páginas web y se convierten en objetos utilizables por LangChain.

2. **División en fragmentos (chunking):**
   El texto se divide en secciones más pequeñas para permitir una búsqueda más eficiente.

3. **Generación de embeddings:**
   Cada fragmento se transforma en una representación numérica (vector) mediante modelos de embeddings.

4. **Almacenamiento vectorial:**
   Los vectores se guardan en una base de datos temporal en memoria para realizar búsquedas por similitud semántica.

5. **Herramientas de recuperación:**
   Se implementa una función que permite buscar y recuperar los fragmentos más relevantes de acuerdo con la consulta del usuario.

6. **Agente inteligente (RAG):**
   Se configura un agente basado en el modelo **Gemini 2.5 Flash Lite**, que usa la herramienta de recuperación para construir respuestas fundamentadas en el contenido del documento.

7. **Middleware dinámico:**
   Se añade una capa que permite al agente incorporar automáticamente contexto relevante a cada consulta, mejorando la precisión de las respuestas.

---

## 🧩 Componentes Principales

| Componente                         | Descripción                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------- |
| **LangChain**                      | Framework principal para construir el agente RAG.                           |
| **Gemini 2.5 Flash Lite**          | Modelo de lenguaje usado para la generación de respuestas.                  |
| **LangSmith**                      | Plataforma de observabilidad para rastrear la ejecución del agente.         |
| **BeautifulSoup (bs4)**            | Utilizado para limpiar y procesar contenido HTML.                           |
| **HuggingFaceEmbeddings**          | Genera los embeddings para el almacenamiento vectorial.                     |
| **InMemoryVectorStore**            | Base de datos temporal en memoria para realizar búsquedas semánticas.       |
| **RecursiveCharacterTextSplitter** | Divide el texto en fragmentos más pequeños para optimizar el procesamiento. |

---

## 🧰 Instalación y Ejecución

### 1. Clonar el repositorio

Ejecuta en tu terminal:

```bash
git clone https://github.com/tu-usuario/Taller-LangChain-LLM.git
cd Taller-LangChain-LLM
```

---

### 2. Instalar dependencias

Instala las librerías necesarias para ejecutar el proyecto:

```bash
pip install langchain langchain-community langchain-text-splitters langchain-google-genai langsmith bs4 sentence-transformers
```

---

### 3. Configurar variables de entorno

Para habilitar el rastreo y la conexión con los servicios externos, debes configurar las variables de entorno.
Estas incluyen las claves de API de **LangSmith** y **Google**.

Ejemplo de configuración:

```bash
LANGSMITH_TRACING "true"
LANGSMITH_API_KEY "tu_api_key_de_langsmith"
GOOGLE_API_KEY "tu_api_key_de_google"
```

> 💡 *Reemplaza las claves con tus valores personales antes de ejecutar el proyecto.*

---

### 4. Ejecutar el notebook o script

Abre el archivo `Guia.ipynb` y ejecuta las celdas en orden para:

1. Cargar y limpiar el documento fuente.
2. Dividir el texto en fragmentos.
3. Generar embeddings y almacenarlos.
4. Crear el agente RAG.
5. Realizar consultas al modelo con contexto dinámico.

---

### 5. Resultados esperados

El agente debe ser capaz de:

* Recuperar fragmentos relevantes del documento según la consulta.
* Generar respuestas completas utilizando el contexto recuperado.
* Incorporar automáticamente nueva información contextual en cada interacción.

---

## 📸 Ejemplo de ejecución

El siguiente ejemplo muestra cómo el agente responde a una pregunta compleja basándose en el contenido del documento cargado:

> **Usuario:** What is task decomposition?
> **Agente:** Task decomposition is the process of breaking a complex goal into smaller, manageable tasks that can be solved sequentially or hierarchically...

*(El resultado puede variar según el modelo y los documentos cargados.)*

---

## 👤 Autor

**Camilo Andrés Quintero Rodríguez**
Proyecto: *Crea un agente RAG con LangChain*


