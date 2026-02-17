from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

Prompt1 = PromptTemplate(
    template="Give me details repot on this {topic}",
    input_variables=['topic']
)

Prompt2 = PromptTemplate(
    template="give me 5 point summary of following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = Prompt1 | model | parser | Prompt2 | model | parser 

result = chain.invoke({'topic' : "artificial intelligence"})

print(result)

chain.get_graph().print_ascii()