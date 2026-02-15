from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pathlib import Path
import json

# Load environment variables from .env
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

# Get the path to the current script's folder
folder = Path(__file__).parent

# Load JSON prompt safely
with open(folder / "promt_Template.json", "r") as f:
    data = json.load(f)

# Create PromptTemplate
template = PromptTemplate(
    template=data["template"],
    input_variables=data["input_variables"]
)

# Example: fill the prompt dynamically
prompt = template.invoke({"topic" : "what is gen ai"})

print(model.invoke(prompt).content)

