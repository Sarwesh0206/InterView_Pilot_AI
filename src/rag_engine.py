from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 8}
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def ask_interview_assistant(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
        You are a senior technical interviewer and placement trainer.

        Answer the question in a detailed manner.

        Context:
        {context}

        Question:
        {question}

        Instructions:

        1. Give a complete explanation.
        2. Explain the concept clearly.
        3. Provide examples.
        4. Mention interview tips.
        5. Mention common mistakes.
        6. Include practical use cases.
        7. Use bullet points.
        8. Write at least 300 words.
        9. Use headings where appropriate.

        Answer:
        """

    response = llm.invoke(prompt)

    return response.content