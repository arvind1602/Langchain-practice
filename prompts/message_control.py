from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

message = [
    SystemMessage(content="you are a my best friend give me any time right suggestion"),
    HumanMessage(content="bro , i want to give up . i fill disappointed after regect in interview")
]

result = model.invoke(message).content

message.append(result)
print(message)