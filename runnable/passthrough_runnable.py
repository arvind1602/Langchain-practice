from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnablePassthrough,passthrough

load_dotenv()

Model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

prompt = PromptTemplate(
    template="give me the 5 line on {topic}",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template="create a linkedIn post caption for this text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="create a twiter(X) post caption for this text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

generate_lines = prompt | Model | parser

parallel_chain = RunnableParallel({
    "topic" : RunnablePassthrough(),
    "linkedIn" : prompt1 | Model | parser,
    "twiter" : prompt2 | Model | parser
})

chain = generate_lines | parallel_chain

result = chain.invoke({"topic": "AI"})

print(result['topic'])
print("\n")
print(result['linkedIn'])
