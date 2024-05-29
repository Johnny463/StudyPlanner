# Personalized Study Plan Generator API

This is a FastAPI application that generates personalized study plans for students based on their academic information and personal needs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- OpenAI API key
- Excel file containing student data (`Studentsdata.xlsx`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Johnny463/StudyPlanner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd StudyPlanner
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:

        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        ```

### Usage

1. Place your student data in an Excel file named `Studentsdata.xlsx` in the project directory. Ensure that the Excel file contains columns for each of the following fields:

    - Name
    - Field of Study
    - Year of Study
    - Subjects Enrolled
    - Personal Objectives
    - Challenges
    - Preferred Learning Styles
    - Extracurricular Activities

2. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

3. Access the Swagger documentation to test the API:

    Open your web browser and go to http://localhost:8000/docs

4. Use the following API endpoints:

    - **GET /generate_study_plans/**: Generates personalized study plans for all students in the Excel file.
    - **POST /generate_study_plan/**: Generates a personalized study plan for a single student. Send student data in the request body.

### Sample Request and Response

#### POST Request

```http
POST /generate_study_plan/

{
  "Name": "John Doe",
  "Field_of_Study": "Computer Science",
  "Year_of_Study": "Sophomore",
  "Subjects_Enrolled": "Database Management, Algorithms, Operating Systems",
  "Personal_Objectives": "Improve problem-solving skills",
  "Challenges": "Balancing coursework with part-time job",
  "Preferred_Learning_Styles": "Visual and hands-on learning",
  "Extracurricular_Activities": "Member of Chess Club, Volunteer at local library"
}

```
## License
MIT License

Copyright (c) 2024 Muhammad Junaid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

