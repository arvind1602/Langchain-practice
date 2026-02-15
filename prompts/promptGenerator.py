from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    please explain the {topic} in such a way .
    1. defination of the topic 
    2. why this is use 
    3. example
    """,
    input_variables=["topic"]
)

template.save("promt_Template.json")