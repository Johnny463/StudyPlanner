from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo", temperature=0)

# Define the prompt template
template = """
As a Academic Advisor and Consultant create a personalized study plan for a student. Here are the details:

Name: {Name} 
Field of Study: {Field_of_study} 
Year of Study: {Year_of_study} 
Subjects Enrolled: {List_of_subjects} 

Personal Needs and Goals:
  Objectives: {Personal_Objectives}
  Challenges: {Challenges}

Preferred Learning Styles: {Preferred_Learning_Styles}


Extracurricular Activities: {Extracurricular_activities}

Based on this information, please generate a personalized study plan that addresses both academic requirements and the student's unique needs and aspirations. 
"""

# Define input data model
class StudentInput(BaseModel):
    Name: str
    Field_of_study: str
    Year_of_study: str
    List_of_subjects: str
    Personal_Objectives: str
    Challenges: str
    Preferred_Learning_Styles: str
    Extracurricular_activities: str

@app.post("/generate_study_plan/")
async def generate_study_plan(student_data: StudentInput):
    try:
        # Create the PromptTemplate
        print(student_data.dict().keys())
        prompt = PromptTemplate(input_variables=list(student_data.dict().keys()), template=template)

        # Create LLMChain
        chain = LLMChain(llm=llm, prompt=prompt)

        # Run the LLMChain to get the AI-generated personalized study plan
        response = chain.run(student_data.dict())
        print(response)

        return {"AI-generated_personalized_study_plan": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/generate_study_plans/")
async def generate_study_plans():
    try:
        # Read data from Excel file
        data = pd.read_excel("Studentsdata.xlsx")
        students = data.to_dict(orient="records")
        
        study_plans = []

        for student in students:
            # Clean student data
            clean_data = {key.replace(' ', '_'): value for key, value in student.items()}
            print(clean_data.keys())
            # Create the PromptTemplate
            prompt = PromptTemplate(input_variables=list(clean_data.keys()), template=template)

            # Create LLMChain
            chain = LLMChain(llm=llm, prompt=prompt)

            # Run the LLMChain to get the AI-generated personalized study plan
            response = chain.run(clean_data)
            
            # Append study plan to the list
            study_plans.append({"Student": clean_data["Name"], "Study_Plan": response})

        return {"Study_Plans": study_plans}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
