from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

class FiveFact(BaseModel):
    fact: list[str] = Field(description="List of five facts")

parser = PydanticOutputParser(pydantic_object=FiveFact)

prompt = PromptTemplate(
    template="""
Give me 5 important facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

chain = prompt | model | parser

result = chain.invoke({"topic": "Generative AI"})

print(result.fact[0])

chain.get_graph().print_ascii()
