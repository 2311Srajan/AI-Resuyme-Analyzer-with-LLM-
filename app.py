import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    try:
        data = request.get_json()
        resume_text = data.get('resume_text', '')
        job_description = data.get('job_description', '')

        if not resume_text or not job_description:
            return jsonify({'error': 'Please provide both resume text and job description.'}), 400

        prompt = f"""
        You are an expert ATS (Applicant Tracking System) resume analyzer.
        Compare the following resume against the job description.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Provide a structured feedback covering:
        1. Overall Match Percentage
        2. Missing Keywords
        3. Key Strengths
        4. Areas for Improvement
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        analysis = response.choices[0].message.content
        return jsonify({'analysis': analysis})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
