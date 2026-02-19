from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

Model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

prompt = PromptTemplate(
    template="give me the 5 line joke on {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,Model ,parser)

print(chain.invoke({"topic" : "AI"}))

