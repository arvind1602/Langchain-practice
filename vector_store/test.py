from langchain_google_genai import GoogleGenerativeAIEmbeddings , ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers.multi_query import MultiQueryRetriever

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


vector_store = Chroma(
    collection_name="dsa",
    embedding_function= embedding_model,
    persist_directory="chroma.db"
)

loader = PyPDFLoader("DSA_QBA.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

# vector_store.add_documents(documents=chunks)

# result = vector_store.similarity_search(query="what is array" , k=3)

retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(),
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
)

result = retriever.invoke("what is tree")

for doc in result :
    print("------")
    print(doc.page_content)