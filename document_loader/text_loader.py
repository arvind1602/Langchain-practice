from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()


loader = TextLoader("cricket.txt")

docs = loader.load()

# print(docs[0])

print(docs[0].page_content)