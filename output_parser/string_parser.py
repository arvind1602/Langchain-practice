from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite"
)

parser = StrOutputParser()

result = model.invoke("how are you")

print(parser.invoke(result))

