from flask import Flask, request, jsonify
from flask_cors import CORS
from extractor import extract_skills

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    skills = extract_skills(file)
    return jsonify({'skills': skills})

if __name__ == '__main__':
    app.run(debug=True)


import fitz  # PyMuPDF

# Sample skill keywords
SKILL_KEYWORDS = {"python", "java", "sql", "react", "flask", "django", "c++", "html", "css", "javascript"}

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_skills(file):
    text = extract_text_from_pdf(file)
    return [skill for skill in SKILL_KEYWORDS if skill in text]

flask
flask-cors
pymupdf
import os
import fitz  # PyMuPDF
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from extractor import extract_skills
from werkzeug.exceptions import BadRequest
from werkzeug.datastructures import FileStorage
from typing import List
from typing import Dict, Any
from typing import Union
from typing import Optional
from typing import Tuple
from typing import Callable

    npm run build
# Upload 'build' directory to Netlify
from flask import Flask, request, jsonify
from flask_cors import CORS
from extractor import extract_skills
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

