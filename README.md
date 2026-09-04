# AI Resume Analyzer

A web application built using Python, Flask, and the GPT-4 API to parse resumes and generate keyword-match insights for job descriptions.

## Tech Stack
* **Backend:** Python, Flask
* **AI Integration:** OpenAI GPT-4 API
* **Deployment:** AWS EC2

## Key Features
* Parses uploaded resumes and extracts core skills and qualifications.
* Compares candidate profiles against targeted job descriptions to generate keyword-match scores.
* Handles API integration and error cases smoothly.

## How to Run
1. Clone the repository: `git clone https://github.com/2311Srajan/AI-Resuyme-Analyzer-with-LLM-.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your OpenAI API key in `.env`
4. Run the application: `python app.py`