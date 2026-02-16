from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated, Literal , Optional

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite"
)

class Student_detail(TypedDict) :
    name: Annotated[str , "must be full "]
    professional_summary : Annotated[str , "summary of his skills and passion"]
    skills : Annotated[list[str] ,'skills']
    mastery : Annotated[str ,"In this stach he/her professional"]
    experience : Optional[str]
    good_command : Literal["MERN" ,"devops" , "ML" , "GenAi" ,"Noting From here"]
    

stucture_model = model.with_structured_output(Student_detail)

result = stucture_model.invoke("""Sneha Kapoor is a motivated and disciplined student who enjoys learning new concepts and improving herself every day. 
She is good at communication, teamwork, problem solving, leadership, and time management. 
She is passionate about personal growth and contributing positively to any organization she joins. 
She considers herself at beginner stage professionally.  """)

print(result)