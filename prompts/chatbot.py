from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",  # exact model name, lowercase, plain dashes
)


chathistory = [
    SystemMessage(content="you are helpful teacher")
]

while True :
    user_input = input("User :- ")  
    if user_input in ['exit' ,'end'] :
        break
    
    chathistory.append(HumanMessage(content=user_input))
    result = model.invoke(chathistory)
    print("Ai :- ", result.content)
    chathistory.append(AIMessage(content=result.content))
    

print("\n",chathistory)