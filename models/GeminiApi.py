from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",  # exact model name, lowercase, plain dashes
)

# Send query
response = model.invoke("summarize attention is all you need documemt 2017 is easy way")

# Print output
print("\n\n")
print(response.content)