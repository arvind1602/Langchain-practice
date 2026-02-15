from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",  # exact model name, lowercase, plain dashes
)

template = PromptTemplate(
    template="give me top 5 coding languages for {domain} domain",
    input_variables=['domain']
)

input = input("enter domain : ")
promp = template.invoke({'domain' : input})


result = model.invoke(promp)

print(result.content)