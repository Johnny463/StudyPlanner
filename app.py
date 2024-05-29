
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = OpenAI(openai_api_key=api_key,model_name="gpt-3.5-turbo-instruct", temperature=0)



template = """
As a Academic Advisor and Consultant create a personalized study plan for a student. Here are the details:

Name: {Name} 
Field of Study: {Field_of_study} 
Year of Study: {Year_of_study} 
Subjects Enrolled: {List_of_subjects} 

**Personal Needs and Goals:**
  * **Objectives:** {Personal_Objectives}
  * **Challenges:** {Challenges}

Preferred Learning Styles: {Preferred_Learning_Styles}


* **Extracurricular Activities:** {Extracurricular_activities}

Based on this information, please generate a personalized study plan that addresses both academic requirements and the student's unique needs and aspirations. 
"""



#input data
data = pd.read_excel("Studentsdata.xlsx")
students = data.to_dict(orient="records")
for student in students:
    # print(student)
    clean_data = {key.replace(' ', '_'): value for key, value in student.items()}
    print(clean_data)

    #PromptTemplate
    prompt = PromptTemplate(input_variables=list(clean_data.keys()), template=template)

    # LLMChain
    chain =LLMChain(llm=llm, prompt=prompt)

    # Run the LLMChain to get the AI-generated personalized study plan
    response = chain.run(clean_data)

    print("AI-generated personalized study plan:")
    print(response)


