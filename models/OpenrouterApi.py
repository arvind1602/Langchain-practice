from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Create the model
llm = ChatOpenAI(
    
    model="openai/gpt-3.5-turbo",
    max_tokens=200,
    # temperature=1

)

# Send a message
print("\n")
response = llm.invoke("explain Ai . also explain ml and dl")
print("\n")

print(response.content)

    