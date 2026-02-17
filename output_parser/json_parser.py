from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite"
)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="give me the name , date of birth , city of the men {men} \n {format}",
    input_variables=["men"],
    partial_variables={"format": parser.get_format_instructions()}
)

chain = prompt | model | parser

print(chain.invoke({"men" : "gandhi"}))