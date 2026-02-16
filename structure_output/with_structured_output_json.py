from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite"
)


student_schema = {
    "title": "Student Details",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "summary": {"type": "string"},
        "skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "professional_stage": {"type": "string"}
    },
    "required": ["name", "summary", "skills", "professional_stage"]
}

stucture_model = model.with_structured_output(student_schema)

result = stucture_model.invoke("""Sneha Kapoor is a motivated and disciplined student who enjoys learning new concepts and improving herself every day. 
She is good at communication, teamwork, problem solving, leadership, and time management. 
She is passionate about personal growth and contributing positively to any organization she joins. 
She considers herself at beginner stage professionally.  """)

print(result)