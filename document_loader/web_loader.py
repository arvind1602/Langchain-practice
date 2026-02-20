from langchain_community.document_loaders import WebBaseLoader
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


url = 'https://passwordsaver.shop'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0])